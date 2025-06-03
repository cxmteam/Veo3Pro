
import streamlit as st

class MonetizationSystem:
    def __init__(self):
        self.name = "Monetization System"
        self.plans = {
            "🆓 Free": {"price": 0, "videos": 5, "features": ["Basic templates", "SD quality"]},
            "⭐ Basic": {"price": 99000, "videos": 25, "features": ["HD quality", "50 templates"]},
            "🚀 Pro": {"price": 199000, "videos": 100, "features": ["4K quality", "All templates", "Priority support"]},
            "👑 Ultimate": {"price": 499000, "videos": "Unlimited", "features": ["Enterprise features", "Custom templates", "API access"]}
        }
    
    def render_monetization_page(self):
        st.markdown("""
        <div style="background: linear-gradient(135deg, rgba(255,255,255,0.1), rgba(255,255,255,0.05)); 
                   backdrop-filter: blur(25px); border: 2px solid rgba(138, 43, 226, 0.3); 
                   border-radius: 25px; padding: 2.5rem; margin-bottom: 2rem; 
                   box-shadow: 0 12px 40px rgba(0, 0, 0, 0.6), inset 0 2px 0 rgba(255, 255, 255, 0.2);">
            <h1 style="color: #FFFFFF;">💰 Hệ thống Monetization</h1>
            <p style="color: #FFFFFF;">Các gói dịch vụ VEO3 Vietnamese Ultimate</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.subheader("💳 Chọn gói phù hợp")
        
        cols = st.columns(len(self.plans))
        
        for i, (plan_name, details) in enumerate(self.plans.items()):
            with cols[i]:
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                           color: white; padding: 1.5rem; border-radius: 15px; text-align: center; margin: 0.5rem 0;">
                    <h3>{plan_name}</h3>
                    <h2>{details['price']:,} VNĐ/tháng</h2>
                    <p>📹 {details['videos']} videos/tháng</p>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown("**✨ Tính năng:**")
                for feature in details['features']:
                    st.markdown(f"- {feature}")
                
                if st.button(f"🛒 Chọn {plan_name.split()[-1]}", key=f"select_{i}"):
                    st.success(f"✅ Đã chọn gói {plan_name}! Liên hệ để thanh toán.")
        
        st.divider()
        st.subheader("💰 Phương thức thanh toán")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.info("📱 **MoMo**\nScan QR để thanh toán")
        with col2:
            st.info("🏦 **Banking**\nChuyển khoản ngân hàng")
        with col3:
            st.info("💳 **Credit Card**\nThẻ tín dụng quốc tế")

def create_monetization_system():
    return MonetizationSystem()
