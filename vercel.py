from chatgpt import app as application

if __name__ == "__main__":
   application.run(debug=True, port=int(os.environ.get('PORT', 8080)))
