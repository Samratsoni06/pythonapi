from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "💕💕😘😘😘 😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘 I love you sweet hart 😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘💕💕"
    }
@app.get("/user")
def get_user():

    data = {
        "id": 1,
        "name": "Samrat"
    }
    return data

@app.get("/p")
def Process():
   return {
    "message": {
        "title": "Complete Git Push & Commit Process After Changes",
        
        "step_1": {
            "title": "Open VS Code Terminal",
            "description": "Open terminal inside VS Code",
            "methods": [
                "Press Ctrl + `",
                "OR Click Terminal > New Terminal"
            ]
        },

        "step_2": {
            "title": "Check Changed Files",
            "description": "See which files are modified before commit",
            "command": "git status",
            "example_output": [
                "modified: app.py",
                "modified: requirements.txt"
            ]
        },

        "step_3": {
            "title": "Add All Changed Files",
            "description": "Stage all updated files for commit",
            "command": "git add ."
        },

        "step_4": {
            "title": "Commit Changes",
            "description": "Save snapshot of current code changes",
            "command": "git commit -m 'updated api changes'",
            "examples": [
                "git commit -m 'added login api'",
                "git commit -m 'fixed database issue'",
                "git commit -m 'updated dashboard api'"
            ]
        },

        "step_5": {
            "title": "Push Code to GitHub",
            "description": "Upload latest code to GitHub repository",
            "command": "git push"
        },

        "step_6": {
            "title": "Automatic Render Deployment",
            "description": [
                "Render automatically detects GitHub changes",
                "Build process starts automatically",
                "Project redeploys automatically",
                "No manual upload required"
            ]
        },

        "step_7": {
            "title": "Check Deployment Status",
            "description": "Open Render dashboard and check deployment logs",
            "url": "https://dashboard.render.com"
        },

        "important_if_new_package_installed": {
            "description": "If you install any new Python package then update requirements.txt before push",
            "example": [
                "pip install sqlalchemy",
                "pip freeze > requirements.txt",
                "git add .",
                "git commit -m 'added sqlalchemy package'",
                "git push"
            ]
        },

        "complete_process_together": [
            "git status",
            "git add .",
            "git commit -m 'updated api'",
            "git push"
        ],

        "important_notes": [
            "Always commit before push",
            "Internet connection required for push",
            "Render redeploy may take 1-3 minutes",
            "Check Render logs if deployment fails"
        ],

        "final_result": {
            "github": "Updated code uploaded successfully",
            "render": "Project automatically redeployed",
            "api": "Latest API changes live on server"
        }
    }
}

