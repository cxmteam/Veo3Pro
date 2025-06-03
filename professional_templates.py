
import streamlit as st

class ProfessionalTemplates:
    def __init__(self):
        self.name = "Professional Templates"
        self.templates = {
            "Ẩm thực Việt": ["Phở Hà Nội", "Bánh mì Sài Gòn", "Cà phê phin"],
            "Du lịch": ["Hạ Long Bay", "Hội An", "Đà Lạt"],
            "Lifestyle": ["Fashion", "Beauty", "Fitness"],
            "Giáo dục": ["Học tiếng Anh", "Kỹ năng mềm", "Công nghệ"],
            "Kinh doanh": ["Startup", "Marketing", "Bán hàng"]
        }
    
    def render_templates_page(self):
        st.markdown("""
        <div style="background: linear-gradient(135deg, rgba(255,255,255,0.1), rgba(255,255,255,0.05)); 
                   backdrop-filter: blur(25px); border: 2px solid rgba(138, 43, 226, 0.3); 
                   border-radius: 25px; padding: 2.5rem; margin-bottom: 2rem; 
                   box-shadow: 0 12px 40px rgba(0, 0, 0, 0.6), inset 0 2px 0 rgba(255, 255, 255, 0.2);">
            <h1 style="color: #FFFFFF;">🎨 Professional Templates</h1>
            <p style="color: #FFFFFF;">150+ mẫu template chuyên nghiệp cho Việt Nam</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Search
        search = st.text_input("🔍 Tìm template:", placeholder="VD: phở, du lịch, tết...")
        
        # Categories
        st.subheader("📂 Danh mục Templates")
        
        for category, templates in self.templates.items():
            with st.expander(f"🍜 {category} - Templates về {category.lower()}", expanded=False):
                cols = st.columns(min(len(templates), 3))
                for i, template in enumerate(templates):
                    with cols[i % 3]:
                        st.markdown(f"""
                        <div style="background: linear-gradient(135deg, rgba(138, 43, 226, 0.2), rgba(30, 144, 255, 0.2)); 
                                   padding: 1rem; border-radius: 10px; margin: 0.5rem 0; border: 1px solid rgba(255,255,255,0.2);">
                            <h4 style="color: #FFFFFF;">{template}</h4>
                            <p style="color: #CCCCCC;">Template về {template.lower()}</p>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        if st.button(f"👀 Preview", key=f"preview_{template}"):
                            st.success(f"🎬 Preview template '{template}' - Đang phát triển!")
                        
                        if st.button(f"📥 Sử dụng", key=f"use_{template}"):
                            st.success(f"✅ Đã chọn template '{template}'!")

def create_professional_templates():
    return ProfessionalTemplates()
