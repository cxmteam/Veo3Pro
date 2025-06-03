
import streamlit as st
from datetime import datetime

class CommunityMarketing:
    def __init__(self):
        self.name = "Community Marketing"
        self.posts = [
            {"user": "NguyenVanA", "content": "Vừa tạo video về phở Hà Nội! AI có tips để làm video ẩm thực hấp dẫn hơn không? 🍜", "likes": 45, "comments": 12, "shares": 8},
            {"user": "ThiThiB", "content": "Contest tháng này có gì hot không mọi người? Mình muốn tham gia! 🏆", "likes": 32, "comments": 18, "shares": 5},
            {"user": "creator123", "content": "Tips tạo content viral: 1) Thumbnail bắt mắt 2) Hook đầu video 3) CTA cuối video ✨", "likes": 78, "comments": 23, "shares": 15}
        ]
    
    def render_community_marketing_page(self):
        st.markdown("""
        <div style="background: linear-gradient(135deg, rgba(255,255,255,0.1), rgba(255,255,255,0.05)); 
                   backdrop-filter: blur(25px); border: 2px solid rgba(138, 43, 226, 0.3); 
                   border-radius: 25px; padding: 2.5rem; margin-bottom: 2rem; 
                   box-shadow: 0 12px 40px rgba(0, 0, 0, 0.6), inset 0 2px 0 rgba(255, 255, 255, 0.2);">
            <h1 style="color: #FFFFFF;">🌐 Community & Marketing</h1>
            <p style="color: #FFFFFF;">Cộng đồng sáng tạo nội dung Việt Nam</p>
        </div>
        """, unsafe_allow_html=True)
        
        tab1, tab2, tab3 = st.tabs(["👥 Community Feed", "🏆 Contest", "📊 Analytics"])
        
        with tab1:
            st.subheader("📝 Tạo bài đăng mới")
            with st.expander("✍️ Tạo bài đăng mới", expanded=False):
                new_post = st.text_area("💭 Bạn đang nghĩ gì?", placeholder="Chia sẻ ý tưởng, kinh nghiệm...")
                if st.button("📤 Đăng bài"):
                    if new_post:
                        st.success("✅ Đã đăng bài thành công!")
                    else:
                        st.warning("Vui lòng nhập nội dung!")
            
            st.subheader("📰 Community Feed")
            for post in self.posts:
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, rgba(138, 43, 226, 0.1), rgba(30, 144, 255, 0.1)); 
                           padding: 1rem; border-radius: 10px; margin: 1rem 0; 
                           border-left: 4px solid rgba(138, 43, 226, 0.8); backdrop-filter: blur(10px);">
                    <h4 style="color: #FFFFFF;">👤 {post['user']}</h4>
                    <p style="margin: 0.5rem 0; color: #CCCCCC;">{post['content']}</p>
                    <div style="display: flex; gap: 1rem; margin-top: 1rem;">
                        <span style="color: #FFFFFF;">👍 {post['likes']}</span>
                        <span style="color: #FFFFFF;">💬 {post['comments']}</span>
                        <span style="color: #FFFFFF;">🔄 {post['shares']}</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        with tab2:
            st.subheader("🏆 Contest VEO3 - Giải thưởng 50M VNĐ")
            st.info("🎯 **Chủ đề:** Tạo video về văn hóa Việt Nam")
            st.info("⏰ **Thời gian:** 1/1/2024 - 31/1/2024")
            st.info("🏆 **Giải thưởng:** Tổng 50,000,000 VNĐ")
            
            if st.button("🎮 Tham gia Contest"):
                st.success("🎉 Đã đăng ký tham gia contest thành công!")
        
        with tab3:
            st.subheader("📊 Marketing Analytics")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("👥 Community Members", "12,584", "+1,234")
            with col2:
                st.metric("📝 Posts Today", "156", "+23")
            with col3:
                st.metric("🔥 Engagement Rate", "8.9%", "+0.5%")

def create_community_marketing():
    return CommunityMarketing()
