# 🌐 AI Website Summarizer

An AI-powered web application that summarizes any website into a concise, easy-to-read overview in seconds.

Simply paste a URL, and the app extracts the webpage content, sends it to a Large Language Model (LLM), and returns a clean summary—all through an intuitive Gradio interface.

## ✨ Features

* 🔗 Summarize any publicly accessible website
* ⚡ Fast and concise AI-generated summaries
* 🎨 Simple and user-friendly Gradio interface
* 🤖 Powered by a Large Language Model
* 🐍 Built entirely in Python

## 🚀 Demo

> Paste any website URL and get a summary in seconds.

<img width="1286" height="353" alt="image" src="https://github.com/user-attachments/assets/15852a9b-305b-41ae-8b05-2e2ad6f02a08" />


## 🛠️ Tech Stack

* Python
* Gradio
* BeautifulSoup
* Requests
* OpenAI API *(or your LLM provider)*
* python-dotenv

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**macOS/Linux**

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
OPENAI_API_KEY=your_api_key_here
```

If you're using another provider (Gemini, Anthropic, Groq, etc.), replace the environment variable accordingly.

## ▶️ Run the App

```bash
python app.py
```

Or, if your main file has a different name:

```bash
python your_file.py
```

The Gradio interface will open in your browser.

## 📂 Project Structure

```text
.
├── app.py
├── requirements.txt
├── .env
├── README.md
└── assets/
```

## ⚙️ How It Works

1. Accept a website URL from the user.
2. Fetch the webpage content.
3. Extract readable text from the HTML.
4. Send the extracted content to an LLM.
5. Display a concise summary through Gradio.

## 💡 Future Improvements

* Support PDF summarization
* Browser extension
* Multi-language summaries
* Adjustable summary length
* Key takeaways & bullet points
* Export summaries as PDF or Markdown
* Chat with a webpage

## 🤝 Contributing

Contributions, suggestions, and feature requests are welcome.

Feel free to fork the repository, create a new branch, and submit a pull request.

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub. It really helps and motivates me to build more AI projects!

Happy coding! 🚀
