# 🍻 College Bars Tracker

Welcome to the **College Bars Tracker**!  
This website helps you keep track of which Cambridge college bars you've attended, rate your experiences, and view your stats — all in your browser using local storage. 🎉

---

## 🚀 Features

- ✅ **Track Attendance:**  
  Each college bar has a counter for how many times you've visited.

- ⭐ **Rate Your Experience:**  
  For each visit, you can rate:
  - Overall experience
  - Atmosphere
  - Value for money
  - Drink selection
  - Who you went with

- 📊 **Statistics:**  
  View your attendance and ratings in easy-to-read charts.

- 💾 **Local Storage:**  
  All your data is saved in your browser. No account needed!

- 🗂️ **Backup & Restore:**  
  Download your data as a backup and restore it anytime.

---

## 🗃️ How Data is Stored

- Local storage contains a key for each college, with the value being the number of times you've attended that bar (defaults to zero).
- Each bar also has a key for detailed entries, stored as a JSON array of visit objects (with ratings, comments, etc).
- The list of colleges is stored in local storage as `"college_list"` (a JSON array), and is loaded by all pages.

---

## 🛟 Backup & Restore

- **Backup:** Click the "Download Backup" button to save your data as a `.json` file.
- **Restore:** Use the "Restore Backup" button to upload a previously saved backup.

---

## 📝 Tech Stack

- HTML, CSS, JavaScript
- [Chart.js](https://www.chartjs.org/) for statistics

---

Enjoy tracking your Cambridge bar adventures! 🍺🍷🥂