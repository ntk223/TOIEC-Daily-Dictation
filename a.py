import json
import os

# TOPIC_MAPPING được tối ưu dựa trên chính các Title trong file JSON của bạn
TOPIC_MAPPING = {
    # L1-5: Tập trung vào các bài thảo luận, hợp đồng, hội thảo
    "General Business (L1-5)": ["contract", "marketing", "warranty", "planning", "conference", "m&a", "acquisition", "workshop", "merger", "agreement"],
    
    # L6-10: Các bài về hỏng máy móc, IT, email (Dựa trên: Office Copier Breakdown, WiFi Connection)
    "Office Issues (L6-10)": ["copier", "shredder", "projector", "wifi", "intranet", "software", "email", "phone line", "equipment", "maintenance", "troubles", "breakdown"],
    
    # L11-15: Nhân sự (Dựa trên: Job Offer, Interview, Internship, Retirement)
    "Personnel (L11-15)": ["interview", "job offer", "internship", "retirement", "hiring", "recruitment", "promotion", "bonus", "supervisor", "receptionist", "salary", "benefit"],
    
    # L16-20: Mua sắm & Giao hàng (Dựa trên: Expedited Shipping, Package Delivery, Purchase Requisition)
    "Purchasing (L16-20)": ["shipping", "delivery", "parcel", "package", "invoice", "receipt", "inventory", "order", "purchase", "warehouse", "expedited"],
    
    # L21-25: Tài chính (Dựa trên: Home Mortgage, Bank Account, Investment, Tax)
    "Financing & Budgeting (L21-25)": ["banking", "account", "mortgage", "investment", "tax", "stock", "financial", "budget", "loan", "debit card"],
    
    # L26-30: Quản lý & Thuê mướn (Dựa trên: Condo Presale, Office Expansion, Lease Termination)
    "Management Issues (L26-30)": ["condo", "presale", "expansion", "lease", "renting", "property", "board meeting", "committee", "quality control"],
    
    # L31-35: Nhà hàng & Sự kiện (Dựa trên: Restaurant Reservation, Coffee Order Mix-Up, Specialty Pizza)
    "Restaurants & Events (L31-35)": ["restaurant", "cafe", "pizza", "coffee", "menu", "reservation", "catering", "party", "festival", "barbecue", "baking", "dessert"],
    
    # L36-40: Du lịch (Dựa trên: Airport Check-in, Flight Delay, Rental Car)
    "Travel (L36-40)": ["airport", "flight", "check-in", "airline", "train", "bus", "rental car", "luggage", "boarding", "travel", "sightseeing"],
    
    # L41-45: Giải trí & Truyền thông (Dựa trên: Musical Tickets, National Portrait Gallery, Art Exhibit)
    "Entertainment (L41-45)": ["musical", "ticket", "gallery", "exhibit", "museum", "concert", "media", "novel", "film", "cinema", "show"],
    
    # L46-50: Y tế & Sức khỏe (Dựa trên: Dental Claim, Dentist Appointment, Pharmacy Prescription)
    "Health (L46-50)": ["dental", "dentist", "pharmacy", "prescription", "medical", "hospital", "clinic", "doctor", "flu shot", "bloodwork", "therapist"]
}

def classify_title(title):
    title_lower = title.lower()
    for topic, keywords in TOPIC_MAPPING.items():
        if any(word in title_lower for word in keywords):
            return topic
    return "Miscellaneous (Cần kiểm tra lại)"

def main():
    if not os.path.exists('listening.json'):
        print("❌ Không thấy file 'listening.json'. Hãy copy file đó vào đây!")
        return

    with open('listening.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    results = {topic: [] for topic in TOPIC_MAPPING.keys()}
    results["Miscellaneous (Cần kiểm tra lại)"] = []

    for item in data:
        cat = classify_title(item['title'])
        results[cat].append(item)

    with open('toeic_classified.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)

    print("🚀 Đã xử lý xong!")
    for topic, items in results.items():
        print(f"- {topic}: {len(items)} bài")

if __name__ == "__main__":
    main()