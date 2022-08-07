import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import MinMaxScaler  

def load_model():
    mLink = './model.pkl'
    with open(mLink, 'rb') as file:
        pipeline = pickle.load(file)
    return pipeline

pipeline = load_model()

model = pipeline['model']
enc_cpu = pipeline['enc_cpu']
enc_gpu = pipeline['enc_gpu']
enc_bt = pipeline['enc_bt']
enc_wc = pipeline['enc_wc']
scaler = pipeline['scaler']
cpu_train = pipeline['cpu']
cpu_train.reverse()
gpu_train = pipeline['gpu']
gpu_train.reverse()
col = pipeline['col']

def predict(model, input_df):
    y_pred = model.predict(input_df)
    return y_pred[0]

st.title('📈 Laptop Prices Prediction 💻')
st.markdown('_[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/syunar/22-01_Laptops-Prices-Prediction-Analysis)_')

mem_size = st.selectbox('ram_size [GB]',(4, 8, 12, 16, 32, 48, 64), index=1)
ssd_size = st.selectbox('ssd_size [GB]',(0, 128, 256, 512, 1000, 1500, 2000, 3000, 4000), index=3)
cpu = st.selectbox('cpu',cpu_train, index=0)
gpu = st.selectbox('gpu',gpu_train, index=0)
resolution = st.selectbox('resolution [px]',('1366x768', '1600x900', '1920x1080', '2304x1440', '2560x1440', '2560x1600', '2880x1800', '3000x2000', '3200x1800', '3840x2160'), index=1)
weight = st.slider("weight [kg]: ", min_value=0.4, max_value=5.0, value=1.8, step=0.1)
refresh_rate = st.selectbox("refresh_rate [Hz]: ", (60, 90, 120, 144, 165, 240, 300, 360), index=1)
size = st.slider("size [inch]: ", min_value=10, max_value=18, value=15, step=1)

with st.expander("Additional Details"):
    web_camera = st.selectbox('web_camera',['none','Below HD', 'HD', '1-2MP', 'FHD', 'Above FHD'], index=2)
    memory_slot = st.selectbox("memory_slot [slots]: ", (0, 1, 2), index=2)
    usbtype_C = st.selectbox('usbtype_C [slots]',(0, 1, 2, 3, 4), index=2)
    hdmi = st.selectbox("hdmi [slots]: ", (0, 1), index=1)
    displayport = st.selectbox('displayport',('0', '1'), index=0)
    bluetooth = st.selectbox('bluetooth',['Bluetooth 5.0', 'Bluetooth 5.1', 'Bluetooth 5.2',
                    'Bluetooth 4.2', 'Bluetooth 4.1', 'Bluetooth 4.0'], index=0)
    warranty = st.selectbox("warranty [year]: ", (0, 1, 2, 3, 4), index=3)

    m2PCIe_slot = st.selectbox("m2PCIe_slot [slots]: ", (0, 1, 2, 3), index=1)
    m2Combo_slot = st.selectbox("m2Combo_slot [slots]: ",(0, 1, 2), index=0)
    m2SATA_slot = st.selectbox("m2SATA_slot [slots]: ", (0, 1), index=0)
    usbtype_A = st.selectbox('usbtype_A [slots]',(0, 1, 2, 3, 4), index=3)
    panel_type = st.selectbox('panel_type',('IPS', 'TN', 'OLED', 'VA'), index=0)
    touch_screen = st.selectbox('touch_screen',('0', '1'), index=0)
    hard_disk_drive = st.selectbox('hard_disk_drive',('0', '1'), index=0)
    d_sub_vga = st.selectbox('d_sub_vga',('0', '1'), index=0)
    thunderbolt = st.selectbox('thunderbolt',('0', '1'), index=0)
    ethernet_lan = st.selectbox('ethernet_lan',('0', '1'), index=0)
    os_bundle = st.selectbox('os_bundle',('Windows 10', 'Windows 11', 'DOS Operating System', 'macOS',
                    'Endless OS', 'Linpus Linux', 'Ubuntu', 'Chrome OS',
                    'Android Pie'), index=0)
    optical_drive = st.selectbox('optical_drive',('0', '1'), index=0)
    fingerprint = st.selectbox('fingerprint',('0', '1'), index=0)
    body_material = st.selectbox('body_material',('Plastic', 'Aluminium + Plastic', 'Aluminium',
                    'Aluminium Alloy', 'Magnesium Alloy', 'Carbon Fiber'), index=0)
    keyboard_backlit = st.selectbox('keyboard_backlit',('0', '1'), index=0)
    numpad = st.selectbox('numpad',('0', '1'), index=0)
    other_detail = st.selectbox('other_detail',('0', '1'), index=0)
    mem_type = st.selectbox('mem_type',('DDR4', 'LPDDR4x', 'DDR5', 'DDR3L', 'LPDDR5', 'LPDDR4',
                    'LPDDR3', 'DDR3'), index=0)
    mem_onboard = st.selectbox('mem_onboard',('0', '1'), index=0)

input_dict = {'size':size,
            'resolution':resolution,
            'refresh_rate':refresh_rate,
            'memory_slot':memory_slot,
            'hdmi':hdmi,
            'weight':weight,
            'warranty':warranty,
            'm2PCIe_slot':m2PCIe_slot,
            'm2Combo_slot':m2Combo_slot,
            'm2SATA_slot':m2SATA_slot,
            'mem_size':mem_size,
            'ssd_size':ssd_size,
            'usbtype_A':usbtype_A,
            'usbtype_C':usbtype_C,
            'panel_type':panel_type,
            'touch_screen':touch_screen,
            'hard_disk_drive':hard_disk_drive,
            'displayport':displayport,
            'd_sub_vga':d_sub_vga,
            'thunderbolt':thunderbolt,
            'ethernet_lan':ethernet_lan,
            'os_bundle':os_bundle,
            'optical_drive':optical_drive,
            'fingerprint':fingerprint,
            'body_material':body_material,
            'keyboard_backlit':keyboard_backlit,
            'numpad':numpad,
            'other_detail':other_detail,
            'mem_type':mem_type,
            'mem_onboard':mem_onboard,
            'cpu':cpu,
            'gpu':gpu,
            'bluetooth':bluetooth,
            'web_camera':web_camera}

df = pd.DataFrame([input_dict])

# resolution
df_res = df['resolution'].str.lower().str.replace(' ','')\
            .str.extract(r'(\d+)[xX]+(\d+)').astype('int')
# convert to numeric [pixel] e.g. 1920x1080 = 2073600 px
df['resolution'] = df_res[0] * df_res[1]


# convert numeric
nums = ['size', 'resolution', 'refresh_rate','memory_slot', 'hdmi',
        'weight', 'warranty', 'm2PCIe_slot', 'm2Combo_slot', 'm2SATA_slot',
        'mem_size', 'ssd_size', 'usbtype_A', 'usbtype_C',
        'displayport',  'touch_screen', 'hard_disk_drive', 'd_sub_vga', 'thunderbolt','ethernet_lan',
        'optical_drive','fingerprint', 'keyboard_backlit',
        'numpad', 'other_detail', 'mem_onboard']
for num in nums:
    df[num] = df[num].apply(pd.to_numeric, errors='coerce')

# one hot encoding
cats = ['panel_type', 'os_bundle','body_material','mem_type']
df = pd.get_dummies(df, columns=cats)

# ordinal encoding
ord_cats = ['cpu', 'gpu', 'bluetooth', 'web_camera']
df[['cpu_enc']] = enc_cpu.transform(df[['cpu']])
df[['gpu_enc']] = enc_gpu.transform(df[['gpu']])
df[['bluetooth_enc']] = enc_bt.transform(df[['bluetooth']])
df[['web_camera_enc']] = enc_wc.transform(df[['web_camera']])
df.drop(ord_cats,axis=1,inplace=True)

df = df.reindex(labels=col,axis=1).fillna(0)

df[nums] = scaler.transform(df[nums])

submit = st.button('Predict')
if submit:
    output = predict(model,df)

    st.success(f'The prices is {output:.2f} baht')
