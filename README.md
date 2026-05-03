# AutoFix-AI
🛠️ Setup Guide
1. Clone the repository
git clone https://github.com/marcosswan-bit/AutoFix-AI.git
cd AutoFix-AI
2. Install dependencies
pip install -r requirements.txt
3. Add your API key 🔑

Create a file called .env in the root folder:

OPENAI_API_KEY=your_api_key_here

Replace your_api_key_here with your actual API key.

4. Create a project folder

This is where your code will be watched:

mkdir project

Create a test file inside it, for example:

# project/test.py
print("hello world")
5. Run the program
python main.py
⚡ How it works
AutoFix AI watches the project/ folder
When you edit a .py file:
It detects the change
Sends the code to the AI
Prints:
Issues found
Explanations
Suggested fixed version
🧪 Example Output
📝 Change detected: test.py

🤖 AI Review:

- Avoid using print() in production code
- Consider using logging instead

Fixed version:
...
⚠️ Notes
This version does not automatically overwrite your files (yet)
It only prints suggestions in the terminal
Requires an internet connection for AI analysis
