from config.conf import pgConn

def create_book(item):
    try:
        create_book_query=f"insert into book_details (book_name,description,number_of_pages,author_name,publisher_name) values('{item.book_name}','{item.description}',{item.number_of_pages},'{item.author_name}','{item.publisher_name}')"
        print(create_book_query)
        cursor=pgConn.cursor()
        cursor.execute(create_book_query)
        pgConn.commit()
        return {"status":"success","message":"Book recored created successfully"}
    except Exception as e:
        return {"status":"Failed","message":f"Book recored creation failes {str(e)}"}
    
def get_book(item):
    try :
        where_clause = []
        if item.author_name:
            where_clause.append(f"author_name = '{item.author_name}'")
        if item.publisher_name:
            where_clause.append(f"publisher_name = '{item.publisher_name}'")
        where_clause_str = " AND ".join(where_clause)
        if where_clause_str:
            get_book_query = f"SELECT * FROM book_details WHERE {where_clause_str}"
        else:
            get_book_query = "SELECT * FROM book_details"
        print(get_book_query)
        cursor=pgConn.cursor()
        cursor.execute(get_book_query)
        columns = [desc[0] for desc in cursor.description]
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return {"status":"success","data":data}
    except Exception as e:
        return {"status":"Failed","message":f"Book recored creation failes {str(e)}"} 
    
def delete_book(item):
    try :
        delete_book_query=f"delete from book_details where bid={item.book_id}"
        print(delete_book_query)
        cursor=pgConn.cursor()
        cursor.execute(delete_book_query)
        pgConn.commit()
        return {"status":"success","message":f"Book record deleted successfully"}
    except Exception as e:
        return {"status":"Failed","message":f"Book record deletion failes {str(e)}"} 