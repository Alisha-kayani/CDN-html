from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Configure the templates directory
templates = Jinja2Templates(directory="templates")

@app.get("/", tags=["Home"])
async def serve_html(request: Request):
    # Renders the index.html file
    return templates.TemplateResponse("index.html", {"request": request})

# The rest of your app's code for running the server would go here
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)