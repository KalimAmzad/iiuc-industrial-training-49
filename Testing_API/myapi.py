# from fastapi import FastAPI

# app = FastAPI()

# # GET= Get an information
# # POST= Create something new
# # PUT= Update an information
# # DELETE= Delete an information

# @app.get("/")
# def index():
#     return {"message": "Hello World"}

# # python -m uvicorn myapi:app --reload


from fastapi import FastAPI

app = FastAPI()

students = {
    1: { "name": "John", "age": 17, "class": "year 12"}, 
    2: {"name": "Mary", "age": 16, "class": "year 11"},
    3: {"name": "Bob", "age": 17, "class": "year 12"},
    4: {"name": "Alice", "age": 16, "class": "year 11"},
    5: {"name": "Richard", "age": 17, "class": "year 12"},
    6: {"name": "Sorowar Mahabub", "age": 24, "class": "year 24"}
}
@app.get("/")
def read_root():
    """
    This function returns a JSON response with a greeting message.

    Returns:
        dict: A dictionary containing a greeting message.
    """
    return {"Hello": "World"}

@app.get("/students/{student_id}")
def read_student(student_id: int):
    """
    This function returns a JSON response with information about a student.

    Args:
        student_id (int): The ID of the student.

    Returns:
        dict: A dictionary containing information about the student.
    """
    if student_id in students:
        return students[student_id]
    else:
        return {"error": "Student not found"}