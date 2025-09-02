# RiskLens - Toxicophore Analyzer and Risk Detector 

A toxicophore is a molecular substructure known to be associated with toxic activity. This tool is based of the dataset from # Balaji S. Metabophore-mediated retro-metabolic ('MeMeReMe') approach in drug design. Drug Discov Today. 2023 Oct;28(10):103736. doi: 10.1016/j.drudis.2023.103736. Epub 2023 Aug 14. PMID: 37586644.

# Main Goals: 
1. Input a Molecule: molecule input is given in the form of SMILES:
2. Search for known toxicophores within the molecule.
3. Risk Assessment:
Red = High-risk toxicophores
Yellow = Moderate-risk toxicophores
Green = No known toxicophores detected

4. Output the risk level, toxicophore names, or highlight them.

# Workflow Description: 

1. Molecule Input is given in the form of SMILES (Simplified Molecular Input Line Entry System)--a way to represent a molecule as a single line of text using letters and symbols that describe atoms and bonds.
2. Then, using a library of known toxicophores, each defined by a name+ SMARTS (SMiles Arbitrary Rarget Transformation Specification) pattern--a language for describing substructures in molecules, used to search for patterns like toxicophores within a chemical structure--SMILES = whole molecule;  SMARTS = chemical pattern you want to search for inside other molecules.
3. The SMILES string is converted into a molecular object (using RDKit or similar), and each SMARTS pattern is applied to this molecule to check if the corresponding toxicophore substructure is present. If a match is found, the toxicophore is flagged.
4. Risk Scoring & Output: Aggregate the detected toxicophores; Assign an overall risk level (based on highest risk match); Display the toxicity flags; matched toxicophore names; and optionally the highlighted regions.

#Example: 

Input SMILES: CC1=CC=CC=C1[N+](=O)[O-] (nitrotoluene)
Detected Toxicophore(s): Aromatic Nitro
Risk Level: 🔴 High

#Limitations: 
1. Only screens against predefined SMARTS patterns
2. No 3D geometry or metabolism-aware analysis
3. Visualization highlighting not yet implemented
