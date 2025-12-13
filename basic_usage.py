"""
Basic Usage Example
===================

This script demonstrates the core features of the
Supply Chain Intelligence System.

Perfect for:
- First-time users
- Quick demos
- Understanding basic functionality
"""

from supply_chain_intelligence import SupplyChainIntelligence

def main():
    print("="*80)
    print("🎯 BASIC USAGE EXAMPLE")
    print("="*80)
    
    # Step 1: Initialize the system
    print("\n1️⃣ Initializing system...")
    system = SupplyChainIntelligence(
        data_file="../data/supply_chain_data.xlsx",
        use_ai=True  # Set to False to disable AI and run faster
    )
    
    # Step 2: Ask questions
    print("\n2️⃣ Asking questions...")
    
    questions = [
        "What is the safety stock policy?",
        "What should I do if a supplier is late?",
        "How do I calculate reorder points?"
    ]
    
    for question in questions:
        print(f"\n{'='*60}")
        result = system.query(question)
        print()
    
    # Step 3: Generate a forecast
    print("\n3️⃣ Generating demand forecast...")
    forecast = system.forecast_demand("SKU0", days=30)
    
    print(f"\n📊 Forecast Summary:")
    print(f"  SKU: {forecast['sku_id']}")
    print(f"  Average: {forecast['metrics']['forecast_avg']:.1f} units/day")
    print(f"  Trend: {forecast['metrics']['trend']}")
    print(f"  Growth: {forecast['metrics']['growth_rate']:+.1f}%")
    print(f"  Recommendation: {forecast['recommendations']['action']}")
    
    # Step 4: Analyze risks
    print("\n4️⃣ Analyzing risks...")
    risks = system.analyze_risks(top_n=10)
    
    print(f"\n⚠️  Risk Summary:")
    print(risks[['sku', 'risk_level', 'risk_score', 'action']])
    
    print("\n\n✅ Example complete!")
    print("="*80)


if __name__ == "__main__":
    main()
