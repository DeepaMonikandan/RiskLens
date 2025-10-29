import streamlit as st
from rdkit import Chem
from rdkit.Chem import Draw

# Toxicophore Patterns 
TOXICOPHORES = [
    {"name": "Aromatic Nitro", "smarts": "[NX3](=O)=O", "risk": "High"},
    {"name": "Aniline", "smarts": "c1ccc(cc1)N", "risk": "Moderate"},
    {"name": "Epoxide", "smarts": "C1OC1", "risk": "High"},]

RISK_LEVELS = {"High": "🔴 High", "Moderate": "🟡 Moderate", "None": "🟢 None"}

def analyze(smiles):
    mol = Chem.MolFromSmiles(smiles)
    if not mol:
        return "Invalid SMILES", [], None

    matches = []
    for tox in TOXICOPHORES:
        pattern = Chem.MolFromSmarts(tox["smarts"])
        if mol.HasSubstructMatch(pattern):
            matches.append(tox)

    if matches:
        max_risk = max(matches, key=lambda x: ["None", "Moderate", "High"].index(x["risk"]))["risk"]
    else:
        max_risk = "None"

    return RISK_LEVELS[max_risk], [m["name"] for m in matches], mol

# Streamlit UI
st.title("Toxic: Toxicophore Analyzer")

smiles = st.text_input("Enter a SMILES string:")
if smiles:
    risk, found, mol = analyze(smiles)
    st.write("### Risk Level:", risk)

    if found:
        st.write("**Detected Toxicophores:**")
        for name in found:
            st.write("- " + name)
        st.image(Draw.MolToImage(mol, size=(300, 300)))
    else:
        st.success("No known toxicophores detected.")

