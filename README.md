# Prices Prediction
![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)(https://syunar-22-01-laptops-prices-prediction-analysis-app-wep6ow.streamlitapp.com/)
## Problem:
ยอดขายตกลง อาจจะเกิดได้จากหลายสาเหตุ หนึ่งในสาเหตุนั้นก็คือกลไกลการตั้งราคาขายของสินค้า
- เพื่อที่จะเพิ่มประสิทธิภาพในการตั้งราคาขาย
- ไม่รู้ว่าควรจะตั้งราคาเท่าไหร่?
- ขายได้แต่ไม่มีกำไรเพราะตั้งราคาต่ำเกินไป
- ขายไม่ออกเนื่องจากราคาสูงเกินไป
- จะลดราคาลงมาก็จะเท่าทุนอยู่แล้ว เหตุจากต้นทุนสูงจนเกินไป

## Ideate:
การใช้ Machine Learning เพื่อประเมินราคาขาย โดยการใส่ input เป็น ลักษณะของสินค้า เช่น specs, types, grades ของสินค้า และมี output เป็นราคาขาย
- เพื่อประเมินราคาขายจากปัจจัยของสินค้านั้นๆ
- ตรวจสอบดูว่าแต่ละปัจจัยหรือตัวแปรส่งผลต่อราคามากน้อยแค่ไหน เพื่อนำไปเปรียบเทียบกับต้นทุนในแต่ละตัวแปรและตรวจสอบดูว่าเราลงทุนไปกับปัจจัยที่ส่งผลต่อราคาได้มีประสิทธิภาพหรือไม่

สำหรับโปรเจคนี้จะเป็นการทำนายราคาของโน้ตบุ๊ค โดยมีขั้นตอนดังนี้

## Steps/Pipeline:
0. Understand Problems
1. Data Collection
    - ใช้การ WebScraping เว็บไซต์ notebookspec.com [(see code)](https://github.com/syunar/22-01_Laptops-Prices-Prediction-Analysis/blob/main/22_01_01_webscraping.ipynb)  เป็นเว็บไซต์เกี่ยวกับคอมพิวเตอร์ โดยจะมีสเปกและราคาของทุกแบรนด์ ซึ่งจำเป็นอย่างมากในการตั้งราคาขาย โดยดูจากราคาตลาดด้วย 
2. Data Cleaning
    - Clean column names
    - Handle missing values
    - Feature extraction: Regex
    - Handle duplicated datas
    - Handle outliers
    - Feature Engineering
    
3. Feature Scaling and Split dataset
    - Feature Selection
    - train test split
    - Feature Scaling
4. Train, Test Model (Base line)
5. Improve Model Perfomanace
    - Compare to other models
    - Hyperparameter tuning
6. Feature Importance
7. Deploy web app [(see code)](https://github.com/syunar/22-01_Laptops-Prices-Prediction-Analysis/blob/main/app.py)
    webapp -> [Laptop Prices Prediction](https://syunar-22-01-laptops-prices-prediction-analysis-app-wep6ow.streamlitapp.com/)

