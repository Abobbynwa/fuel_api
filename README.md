
---

# 🚀 **Fuel Route Optimization API**  

A Django-based REST API that calculates the most **cost-effective** and **efficient** route for a vehicle traveling between two locations in the **USA**. The API factors in:  
✅ **Optimized route calculation** using **OpenRouteService**  
✅ **Fuel stops based on real-time fuel prices**  
✅ **Vehicle constraints** (500-mile max range, 10 MPG fuel efficiency)  
✅ **Minimal API calls for efficiency**  

---

## 📌 **Tech Stack**
- **Django 3.2.23** (Web framework)  
- **Django REST Framework** (API development)  
- **OpenRouteService API** (For routing and map data)  
- **Pandas** (For processing fuel price data)  
- **Postman & cURL** (For API testing)  

---

## 📌 **Installation & Setup**  

### **1️⃣ Clone the Repository**  
```sh
git clone https://github.com/Abobbynwa/fuel_api.git
cd fuel_api
```

### **2️⃣ Create & Activate Virtual Environment**  
```sh
python3 -m venv myenv
source myenv/bin/activate  # (For macOS/Linux)
myenv\Scripts\activate     # (For Windows)
```

### **3️⃣ Install Dependencies**  
```sh
pip install -r requirements.txt
```

### **4️⃣ Apply Migrations**  
```sh
python manage.py migrate
```

### **5️⃣ Start the Development Server**  
```sh
python manage.py runserver
```
Your API will now be running at:  
🔗 **http://127.0.0.1:8000/**  

---

## 📌 **API Endpoints**
| Method | Endpoint | Description |
|---------|-----------------|-------------|
| **POST** | `/api/route/` | Calculate the best route and fuel stops |
| **GET** | `/api/docs/` | API documentation (if enabled) |

### **Example Request (cURL)**
```sh
curl -X POST "http://127.0.0.1:8000/api/route/" \
     -H "Content-Type: application/json" \
     -d '{
           "start": "New York, NY",
           "end": "Los Angeles, CA"
         }'
```

---

## 📌 **Deployment**
### **Deploy on Render**
To deploy this API to **Render**, follow these steps:
1. **Push your code to GitHub** (Done ✅)
2. **Sign up on Render** → [https://render.com/](https://render.com/)
3. **Create a new web service**
4. **Connect your GitHub repo (`fuel_api`)**
5. Set the **Build Command**:
   ```sh
   pip install -r requirements.txt
   ```
6. Set the **Start Command**:
   ```sh
   gunicorn fuel_api.wsgi:application
   ```
7. **Deploy & Get Your Live API URL!** 🎉  

---

## 📌 **License**
This project is **open-source** and available under the **MIT License**.

---

## 📌 **Author**
👨‍💻 **Developed by:** Valentine Agaba  
📧 Contact: [valentineagaba22@gmail.com](mailto:valentineagaba22@gmail.com)  
🔗 GitHub: [@Abobbynwa](https://github.com/Abobbynwa)  

---

