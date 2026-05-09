# LibTrack API Platform

## Project Overview
LibTrack is a Smart Library & Book Inventory Management System developed using Flask and SQLite.

The system helps educational institutes manage:

- Books
- Members
- Borrow/Return Records
- Inventory
- CSV Uploads
- Analytics
- Audit Logs

---

## Technologies Used

- Python
- Flask
- SQLite
- Pandas
- REST APIs

---

## Features

- Add/View/Delete Books
- Add/View Members
- Borrow & Return Books
- Inventory Tracking
- CSV Upload Support
- Reading Analytics
- Audit Logs

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | / | Home |
| POST | /books | Add Book |
| GET | /books | Get Books |
| DELETE | /books/<id> | Delete Book |
| POST | /members | Add Member |
| GET | /members | Get Members |
| POST | /borrow | Borrow Book |
| PUT | /return/<id> | Return Book |
| POST | /upload-books | Upload CSV |
| GET | /analytics | Analytics |
| GET | /logs | Audit Logs |

---

## Run Project

```bash
pip install -r requirements.txt
python app.py