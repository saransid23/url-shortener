# 🔗 URL Shortener Web App (Flask + Render)

## 📌 Project Overview

This is a simple and efficient **URL Shortener Web Application** built using **Flask** and deployed on the cloud using **Render**. The application allows users to convert long URLs into short, manageable links and redirect them easily.

---

## 🚀 Features

* 🔗 Shorten long URLs instantly
* 📋 Copy shortened URL to clipboard
* 🌐 Redirect to original URL
* 💎 Modern UI with glassmorphism design
* ☁️ Cloud deployment using Render

---

## 🛠️ Technologies Used

* **Frontend:** HTML, CSS
* **Backend:** Python (Flask)
* **Database:** SQLite
* **Deployment:** Render
* **Version Control:** GitHub

---

## 📁 Project Structure

```
url-shortener/
│── app.py
│── requirements.txt
│── Procfile
│── urls.db
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```
git clone https://github.com/your-username/url-shortener.git
cd url-shortener
```

### 2️⃣ Create Virtual Environment

```
python -m venv venv
```

### 3️⃣ Activate Virtual Environment

**Windows:**

```
venv\Scripts\activate
```

**Mac/Linux:**

```
source venv/bin/activate
```

### 4️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```
python app.py
```

Open your browser and go to:

```
http://127.0.0.1:5000/
```

---

## ☁️ Deployment (Render)

1. Push your project to GitHub
2. Go to Render Dashboard
3. Click **New → Web Service**
4. Connect your GitHub repository

### 🔧 Configuration:

* **Build Command:**

```
pip install -r requirements.txt
```

* **Start Command:**

```
gunicorn app:app
```

5. Click **Deploy**

---

## 🧪 Testing

| Input URL          | Output        |
| ------------------ | ------------- |
| https://google.com | Shortened URL |
| Invalid Code       | URL not found |

---

## 📊 Example Output

```
https://your-app.onrender.com/aB12Cd
```

Clicking the link redirects to the original URL.

---

## 🎯 Future Enhancements

* 📈 Click analytics dashboard
* 🔐 User authentication system
* 📝 Custom short URLs
* 📱 Mobile responsive improvements

---

## 👩‍💻 Author

**Saran Siddarth**

---

## 📜 License

This project is for educational purposes.

---

## ⭐ Acknowledgement

Built as part of a **Cloud Computing / AI & Data Science project**.
