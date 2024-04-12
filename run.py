import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from routers import book_details_urls, auth_urls
from fastapi.responses import JSONResponse

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_urls.router)
app.include_router(book_details_urls.router)

from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
import logging

logger = logging.getLogger(__name__)

async def validate_request(request: Request, call_next):
    try:
        # Read and parse the request body as JSON
        request.state.payload = await request.json()
        logger.debug("Request body: %s", request.state.payload)

        # Perform validation if needed
        if not request.state.payload:
            raise HTTPException(status_code=400, detail="Request body is empty")

        # Call the next middleware or endpoint handler
        response = await call_next(request)
        return response

    except ValueError:
        # Empty or invalid request body
        logger.exception("Error parsing request body")
        return JSONResponse(status_code=400, content={"message": "Invalid request body"})

    except HTTPException as http_exc:
        # HTTPException raised by validation logic
        logger.exception("Error validating request")
        return http_exc

    except Exception as e:
        # Other unexpected errors
        logger.exception("Internal server error")
        return JSONResponse(status_code=500, content={"message": "Internal server error"})



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
