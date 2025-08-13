## **📌 Overview**

They want you to build a **Weather App** in **two stages**:

1. **Tech Assessment 1** → Basic working weather app (real-time data from APIs, nice presentation, optional extras like 5-day forecast).
2. **Tech Assessment 2** → Advanced version with:

   * Database storage
   * CRUD (Create, Read, Update, Delete) operations
   * Extra API integrations (Google Maps, YouTube, etc.)
   * Optional data export (JSON, CSV, PDF, Markdown)

Both stages test your **coding skills**, **creativity**, and **user experience design thinking**.

---

## **Step-by-Step Breakdown**

### **🔹 Part 1: Tech Assessment 1 (Basic Weather App)**

**Goal:**
Make an app where a user can:

* **Enter a location** → could be Zip code, City, GPS coordinates, or even landmarks.
* **Get current weather** for that location (from an actual API — not static/fake data).
* Display weather clearly, with **useful details** (temperature, humidity, conditions, wind speed, etc.).

**Bonus (to stand out):**

* Show a **5-day forecast**.
* Let the user see **weather for their current location** automatically.
* Use **icons/images** to make it visually appealing.

**Restrictions:**

* Any **tech stack** is fine (React, Python Flask, Node.js, etc.).
* UI **doesn’t have to be pretty**, but functional.
* Must **pull real data from an API** like [OpenWeatherMap](https://openweathermap.org/api).

---

### **🔹 Part 2: Tech Assessment 2 (Advanced Weather App)**

**Goal:**
Enhance your Part 1 app by adding **data persistence and more features**.

#### **2.1 CRUD with Database (Required)**

Pick **SQL** (MySQL, PostgreSQL, SQLite) or **NoSQL** (MongoDB, Firebase) and:

* **CREATE:**
  User enters a **location + date range**, app stores the **temperature for that range** in the database.
  Must validate:

  * Date range is valid
  * Location exists (or use fuzzy matching to guess)

* **READ:**
  User can retrieve **any previously stored weather info** (even from other users).

* **UPDATE:**
  User can **edit** stored weather info (decide which fields are editable).
  Again, validate the new data.

* **DELETE:**
  User can delete any stored record.

---

#### **2.2 API Integration (Optional but impressive)**

Add **extra APIs** to make it more useful:

* **YouTube API** → Show videos of the location.
* **Google Maps API** → Show location on a map.
* Any creative API that adds value (like sunrise/sunset times, air quality, etc.).

---

#### **2.3 Data Export (Optional but impressive)**

Let users export their stored data in formats like:

* **JSON**
* **XML**
* **CSV**
* **PDF**
* **Markdown**

---

### **🔹 Submission Requirements**

1. **GitHub Repo**

   * Public repo with code + README explaining:

     * How to run the app
     * What tech stack you used
   * Include `requirements.txt` (Python) or `package.json` (Node.js).
   * If private, give access to `PMA-Community`.

2. **Demo Video**

   * 1-2 min screen recording
   * Show how the app meets the requirements
   * Host on Google Drive, YouTube, or Vimeo (public link).

3. **Weather App URL**

   * If deployed online, share the live link.

4. **Info Button in App**

   * Include your name
   * Show company description (from their LinkedIn page).

---

### **📌 Key Points to Remember**

* You can **just do Assessment 1** and still be considered.
* Ideal candidate **also does parts of Assessment 2**.
* Creativity + functionality = higher chance to be shortlisted.
* No fake/static data — **real API calls are required**.
