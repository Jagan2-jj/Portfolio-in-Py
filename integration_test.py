from app import app, db, ContactMessage, mail, Message

with app.app_context():
    print("Running integration test...")
    try:
        # 1. Test Database
        test_msg = ContactMessage(
            name="Test User",
            email="test@example.com",
            subject="Integration Test",
            message="This is a test message to verify the backend integration."
        )
        db.session.add(test_msg)
        db.session.commit()
        print("✅ Database storage test passed.")
        
        # 2. Test Email (Simple check)
        print("Attempting to send a test email...")
        msg = Message(
            subject="Test Email from Portfolio Backend",
            recipients=['jaganpanigrahi2004@gmail.com'],
            body="This is a test email sent during backend integration verification."
        )
        # We catch the exception if credentials are wrong or server blocks it
        mail.send(msg)
        print("✅ Email delivery test passed.")
        
    except Exception as e:
        print(f"❌ Integration test failed: {str(e)}")
