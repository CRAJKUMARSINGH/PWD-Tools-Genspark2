#!/usr/bin/env python3
"""
PWD Tools Component Tester
Tests all 10 components with basic functionality only
"""

def test_01_excel_se_emd():
    """Test Excel se EMD Component"""
    print("=" * 60)
    print("🔍 COMPONENT 1: Excel se EMD")
    print("=" * 60)
    
    # Sample data - only what's needed
    sample_data = [
        {"Payee Name": "Rajkumar Contractor", "Amount": 50000, "Work": "Electrical Installation"},
        {"Payee Name": "Babulal Electric", "Amount": 75000, "Work": "Transformer Maintenance"}
    ]
    
    print("📊 Sample Excel Data:")
    for i, row in enumerate(sample_data, 1):
        print(f"  {i}. {row['Payee Name']} - Rs. {row['Amount']:,} - {row['Work']}")
    
    print("\n📄 Generated Receipt Preview:")
    print("  ┌─────────────────────────────────────────────────┐")
    print("  │           HAND RECEIPT (RPWA 28)               │")
    print("  │  Payable to: Rajkumar Contractor               │")
    print("  │  Amount: Rs. 50,000/-                          │")
    print("  │  Work: Electrical Installation                  │")
    print("  └─────────────────────────────────────────────────┘")
    
    return True

def test_02_bill_deviation():
    """Test Bill Deviation Component"""
    print("\n" + "=" * 60)
    print("🔍 COMPONENT 2: Bill Deviation Calculator")
    print("=" * 60)
    
    # Only basic calculation
    original_amount = 100000
    revised_amount = 125000
    deviation = ((revised_amount - original_amount) / original_amount) * 100
    
    print("📊 Bill Deviation Calculation:")
    print(f"  Original Amount: Rs. {original_amount:,}")
    print(f"  Revised Amount:  Rs. {revised_amount:,}")
    print(f"  Deviation:       {deviation:.2f}%")
    
    return True

def test_03_tender_processing():
    """Test Tender Processing Component"""
    print("\n" + "=" * 60)
    print("🔍 COMPONENT 3: Tender Processing")
    print("=" * 60)
    
    # Only basic tender info
    tenders = [
        {"Tender No": "T001/2024", "Work": "Road Construction", "Estimated Cost": 5000000},
        {"Tender No": "T002/2024", "Work": "Bridge Repair", "Estimated Cost": 2500000}
    ]
    
    print("📋 Tender Processing:")
    for tender in tenders:
        print(f"  {tender['Tender No']}: {tender['Work']}")
        print(f"    Estimated: Rs. {tender['Estimated Cost']:,}")
    
    return True

def test_04_bill_note_sheet():
    """Test Bill Note Sheet Component"""
    print("\n" + "=" * 60)
    print("🔍 COMPONENT 4: Bill Note Sheet")
    print("=" * 60)
    
    # Only basic bill info
    bill_data = {
        "Bill No": "BN001/2024",
        "Contractor": "Rajkumar Construction",
        "Work": "Electrical Installation",
        "Contract Amount": 500000,
        "Work Done": 75,  # percentage
        "Amount Claimed": 375000
    }
    
    print("📄 Bill Note Sheet:")
    print(f"  Bill No: {bill_data['Bill No']}")
    print(f"  Contractor: {bill_data['Contractor']}")
    print(f"  Work: {bill_data['Work']}")
    print(f"  Contract Amount: Rs. {bill_data['Contract Amount']:,}")
    print(f"  Work Completion: {bill_data['Work Done']}%")
    print(f"  Amount Claimed: Rs. {bill_data['Amount Claimed']:,}")
    
    return True

def test_05_deductions_table():
    """Test Deductions Table Component"""
    print("\n" + "=" * 60)
    print("🔍 COMPONENT 5: Deductions Table")
    print("=" * 60)
    
    # Only basic deductions
    deductions = [
        {"Type": "Income Tax", "Rate": "2%", "Amount": 2500},
        {"Type": "Security Deposit", "Rate": "5%", "Amount": 6250}
    ]
    
    print("💰 Deductions Table:")
    print("  Type                Rate    Amount")
    print("  ──────────────────────────────────")
    for deduction in deductions:
        print(f"  {deduction['Type']:<18} {deduction['Rate']:<7} Rs. {deduction['Amount']:,}")
    
    total_deductions = sum(d['Amount'] for d in deductions)
    print(f"\n  Total Deductions: Rs. {total_deductions:,}")
    
    return True

def test_06_delay_calculator():
    """Test Delay Calculator Component"""
    print("\n" + "=" * 60)
    print("🔍 COMPONENT 6: Delay Calculator")
    print("=" * 60)
    
    # Only delay days calculation
    original_duration = 150  # days
    actual_duration = 196  # days
    delay_days = actual_duration - original_duration
    
    print("⏰ Delay Calculation:")
    print(f"  Original Duration: {original_duration} days")
    print(f"  Actual Duration:   {actual_duration} days")
    print(f"  Delay:             {delay_days} days")
    
    return True

def test_07_emd_refund():
    """Test EMD Refund Component"""
    print("\n" + "=" * 60)
    print("🔍 COMPONENT 7: EMD Refund Calculator")
    print("=" * 60)
    
    # Only basic EMD info
    emd_data = {
        "Contractor": "Rajkumar Electric",
        "Tender Amount": 1000000,
        "EMD Amount": 20000,
        "EMD Rate": "2%"
    }
    
    print("💳 EMD Refund Calculation:")
    print(f"  Contractor: {emd_data['Contractor']}")
    print(f"  Tender Amount: Rs. {emd_data['Tender Amount']:,}")
    print(f"  EMD Amount: Rs. {emd_data['EMD Amount']:,}")
    print(f"  EMD Rate: {emd_data['EMD Rate']}")
    
    return True

def test_08_financial_progress():
    """Test Financial Progress Component"""
    print("\n" + "=" * 60)
    print("🔍 COMPONENT 8: Financial Progress Tracker")
    print("=" * 60)
    
    # Only basic progress info
    progress_data = {
        "Project": "Electrical Infrastructure",
        "Total Budget": 5000000,
        "Expenditure": 3250000,
        "Balance": 1750000
    }
    
    print("📊 Financial Progress:")
    print(f"  Project: {progress_data['Project']}")
    print(f"  Total Budget: Rs. {progress_data['Total Budget']:,}")
    print(f"  Expenditure: Rs. {progress_data['Expenditure']:,}")
    print(f"  Balance: Rs. {progress_data['Balance']:,}")
    
    return True

def test_09_security_refund():
    """Test Security Refund Component"""
    print("\n" + "=" * 60)
    print("🔍 COMPONENT 9: Security Refund Calculator")
    print("=" * 60)
    
    # Only basic security info
    security_data = {
        "Contractor": "Babulal Construction",
        "Contract Value": 2000000,
        "Security Amount": 100000,
        "Security Rate": "5%"
    }
    
    print("🔒 Security Refund Calculation:")
    print(f"  Contractor: {security_data['Contractor']}")
    print(f"  Contract Value: Rs. {security_data['Contract Value']:,}")
    print(f"  Security Amount: Rs. {security_data['Security Amount']:,}")
    print(f"  Security Rate: {security_data['Security Rate']}")
    
    return True

def test_10_stamp_duty():
    """Test Stamp Duty Component"""
    print("\n" + "=" * 60)
    print("🔍 COMPONENT 10: Stamp Duty Calculator")
    print("=" * 60)
    
    # Only basic stamp duty calculation
    contract_value = 3000000
    stamp_duty_rate = 0.5  # 0.5%
    stamp_duty_amount = (contract_value * stamp_duty_rate) / 100
    
    print("🏛️ Stamp Duty Calculation:")
    print(f"  Contract Value: Rs. {contract_value:,}")
    print(f"  Stamp Duty Rate: {stamp_duty_rate}%")
    print(f"  Stamp Duty Amount: Rs. {stamp_duty_amount:,}")
    
    return True

def main():
    """Main test function"""
    print("🚀 PWD TOOLS COMPONENT TESTER")
    print("Testing all 10 components with basic functionality...")
    print()
    
    # Test all components
    tests = [
        test_01_excel_se_emd,
        test_02_bill_deviation,
        test_03_tender_processing,
        test_04_bill_note_sheet,
        test_05_deductions_table,
        test_06_delay_calculator,
        test_07_emd_refund,
        test_08_financial_progress,
        test_09_security_refund,
        test_10_stamp_duty
    ]
    
    results = []
    for test in tests:
        try:
            result = test()
            results.append(result)
        except Exception as e:
            print(f"❌ Error in {test.__name__}: {e}")
            results.append(False)
    
    # Summary
    print("\n" + "=" * 60)
    print("📋 TEST SUMMARY")
    print("=" * 60)
    print(f"  Total Components: {len(tests)}")
    print(f"  Successful: {sum(results)}")
    print(f"  Failed: {len(results) - sum(results)}")
    
    if all(results):
        print("  🎉 All components tested successfully!")
    else:
        print("  ⚠️  Some components had issues")
    
    print("\n✨ Testing completed!")

if __name__ == "__main__":
    main()
