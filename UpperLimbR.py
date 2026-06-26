import streamlit as st

st.set_page_config(
    page_title="Shoulder & Upper Limb",
    page_icon="🩺",
    layout="centered"
)

st.title("Shoulder & Upper Limb")
st.caption("Doctor Quick Reminder • Rule-based • No AI")

st.warning(
    "Concise clinical reminder only. Use clinical judgment and local referral guidelines."
)

tab1, tab2 = st.tabs(["🚩 Red Flags", "🧠 Differential Diagnoses"])

with tab1:

    st.subheader("Red Flags")

    st.markdown("""

### General
- Fever or systemic illness
- Rapid swelling
- Severe pain out of proportion
- Open injury
- Immunocompromised patient

### Trauma
- Suspected fracture or dislocation
- Neurovascular compromise
- Compartment syndrome
- Penetrating injury

### Neurologic
- Progressive weakness
- New numbness
- Loss of hand function
- Cervical myelopathy signs

### Infection
- Septic arthritis
- Cellulitis with spreading erythema
- Abscess
- Osteomyelitis

### Vascular
- Cold pale limb
- Absent pulse
- Acute ischemia
- DVT of upper limb

### Malignancy
- Persistent night pain
- Unexplained weight loss
- Enlarging mass
- Pathological fracture

""")

with tab2:

    st.subheader("Differential Diagnoses")

    st.markdown("""

### Shoulder
- Rotator cuff tendinopathy
- Rotator cuff tear
- Impingement syndrome
- Adhesive capsulitis
- Subacromial bursitis
- Glenohumeral OA
- AC joint sprain
- Shoulder instability

### Elbow
- Lateral epicondylitis
- Medial epicondylitis
- Olecranon bursitis
- Ulnar neuropathy

### Wrist / Hand
- Carpal tunnel syndrome
- De Quervain tenosynovitis
- Trigger finger
- Ganglion cyst
- Thumb CMC OA

### Nerve
- Cervical radiculopathy
- Brachial plexopathy
- Peripheral nerve entrapment

### Inflammatory
- Rheumatoid arthritis
- Gout
- Psoriatic arthritis

### Infection
- Cellulitis
- Septic arthritis
- Flexor tenosynovitis

### Others
- Myofascial pain syndrome
- Fibromyalgia
- Referred cardiac pain
- Pancoast tumor

""")

st.divider()

st.caption(
    "KU KPS Infirmary"
)
