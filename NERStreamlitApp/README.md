# ⚠️ App Features
## 🗒️ Input Options:
* Write your own text in a text box
* Upload a .txt file
* Or use the preloaded sample text
## 📢 Define Custom Entities 
Enter customized JSON-style pattern rules for the EntityRuler, like:

{"label": "BUILDING", "pattern": "Golden Dome"}

{"label": "UNIVERSITY", "pattern": "Notre Dame"}

Each pattern should follow spaCy's EntityRuler format. 
## ✨ Output 
* A list of detected entities with their labels
* A visual representation using Displacy highlighting matched terms in color
