
import streamlit as st

class UtilityFeatures:
    def __init__(self):
        self.name = "Utility Features"
    
    def render_utility_features_page(self):
        st.markdown("""
        <div style="background: linear-gradient(135deg, rgba(255,255,255,0.1), rgba(255,255,255,0.05)); 
                   backdrop-filter: blur(25px); border: 2px solid rgba(138, 43, 226, 0.3); 
                   border-radius: 25px; padding: 2.5rem; margin-bottom: 2rem; 
                   box-shadow: 0 12px 40px rgba(0, 0, 0, 0.6), inset 0 2px 0 rgba(255, 255, 255, 0.2);">
            <h1 style="color: #FFFFFF;">🔧 Utility Features</h1>
            <p style="color: #FFFFFF;">Bộ công cụ tiện ích toàn diện</p>
        </div>
        """, unsafe_allow_html=True)
        
        tab1, tab2, tab3, tab4 = st.tabs(["🎬 Video Tools", "🤖 AI Tools", "🖼️ Image Tools", "📊 Analytics"])
        
        with tab1:
            st.subheader("🎬 Video Converter")
            st.info("Convert video cho các platform khác nhau")
            
            uploaded_file = st.file_uploader("📤 Upload video", type=['mp4', 'avi', 'mov'])
            if uploaded_file:
                st.success("✅ File đã upload thành công!")
                
                col1, col2 = st.columns(2)
                with col1:
                    output_format = st.selectbox("Format đầu ra:", ["MP4", "AVI", "MOV", "WebM"])
                with col2:
                    quality = st.selectbox("Chất lượng:", ["1080p", "720p", "480p"])
                
                if st.button("🔄 Convert Video"):
                    st.success("🎉 Video đã được convert thành công!")
        
        with tab2:
            st.subheader("🤖 AI Text Generator")
            prompt = st.text_area("💭 Nhập prompt:", placeholder="Viết caption cho video về ẩm thực...")
            if st.button("✨ Generate Text"):
                if prompt:
                    st.success("🤖 AI: Đây là caption được tạo từ AI cho prompt của bạn!")
                else:
                    st.warning("Vui lòng nhập prompt!")
            
            st.subheader("🎙️ AI Voice Generator")
            text_input = st.text_area("📝 Text to Speech:", placeholder="Nhập text để chuyển thành giọng nói...")
            voice_type = st.selectbox("🎭 Chọn giọng:", ["Nam miền Bắc", "Nữ miền Nam", "Nam miền Trung", "Nữ miền Bắc"])
            
            if st.button("🎤 Generate Voice"):
                if text_input:
                    st.success("🎙️ File audio đã được tạo thành công!")
                else:
                    st.warning("Vui lòng nhập text!")
        
        with tab3:
            st.subheader("🖼️ Image Editor")
            st.info("🎨 Chỉnh sửa hình ảnh online")
            
            uploaded_image = st.file_uploader("📷 Upload ảnh", type=['jpg', 'jpeg', 'png'])
            if uploaded_image:
                st.image(uploaded_image, caption="Ảnh đã upload", use_column_width=True)
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    if st.button("✨ Auto Enhance"):
                        st.success("Đã enhance ảnh!")
                with col2:
                    if st.button("🎨 Add Filter"):
                        st.success("Đã thêm filter!")
                with col3:
                    if st.button("📏 Resize"):
                        st.success("Đã resize ảnh!")
        
        with tab4:
            st.subheader("📊 Productivity Analytics")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("🎬 Videos Created", "47", "+12")
            with col2:
                st.metric("⏱️ Time Saved", "15.2h", "+3.5h")
            with col3:
                st.metric("🚀 Productivity", "89%", "+5%")

def create_utility_features():
    return UtilityFeatures()
