import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.table import Table
from reportlab.platypus import SimpleDocTemplate, Table as PDFTable, TableStyle, Paragraph
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
import os

# Define the data
data = [
    ["*GPR137B*", "Intensification", "Relaxation", "Positively regulates mTORC1 signaling, a central node in nutrient sensing and longevity pathways."],
    ["*LMOD1*", "Intensification", "Relaxation", "Actin nucleator essential for smooth muscle filament assembly and contractility."],
    ["*ANK2*", "Intensification", "Relaxation", "Required for targeting and stabilizing the Na⁺/Ca²⁺ exchanger in cardiomyocytes."],
    ["*MYO18B*", "Intensification", "Relaxation", "Unconventional myosin regulating sarcomere assembly and lysosomal exocytosis; potential tumor suppressor."],
    ["*CYP19A1*", "Intensification", "Relaxation", "Cytochrome P450 enzyme involved in drug metabolism and steroid/lipid biosynthesis."],
    ["*EEF1A1*", "Intensification", "Relaxation", "Eukaryotic elongation factor-1α critical for protein synthesis."],
    ["*GLRX*", "Intensification", "Relaxation", "Glutaredoxin involved in antioxidant defense and implicated in β-amyloid toxicity in Alzheimer’s disease."],
    ["*ABHD3*", "Intensification", "Relaxation", "Function not well-defined; likely involved in lipid metabolism."],
    ["*ADAMTS7*", "Intensification", "Relaxation", "Regulates vascular smooth muscle cell migration; implicated in atherosclerosis."],
    ["*CCT2*", "Intensification", "Relaxation", "Molecular chaperone essential for ATP-dependent protein folding."],
    ["*DUSP10*", "Intensification", "Relaxation", "Negatively regulates MAP kinases involved in cell proliferation and differentiation."],
    ["*MAN2C1*", "Intensification", "Relaxation", "Mannosidase involved in catabolism of oligosaccharides."],
    ["*IL1R1*", "Relaxation", "Intensification", "IL-1 receptor mediating inflammatory signaling via NF‑κB and MAPK activation."],
    ["*PCNX2*", "Relaxation", "Intensification", "Associated with tumors exhibiting high microsatellite instability (MSI-H)."],
    ["*FDPS*", "Relaxation", "Intensification", "Key enzyme in cholesterol and sterol biosynthesis via the mevalonate pathway."],
    ["*LRP2*", "Relaxation", "Intensification", "Endocytic receptor mediating uptake of lipoproteins, hormones, and sterols; modulates Sonic Hedgehog and MAPK signaling."],
    ["*XXYLT1*", "Relaxation", "Intensification", "Glycosyltransferase involved in O-glycan processing and metal ion binding."],
    ["*TRPV1*", "Relaxation", "Intensification", "Ion channel responsive to heat and pain; involved in inflammatory responses."],
    ["*EGFR*", "Relaxation", "Intensification", "Receptor tyrosine kinase essential for cell growth and survival; also linked to inflammatory responses like cytokine storms."]
]

columns = ["Gene", "BMAL", "ELLSM", "Function"]
df = pd.DataFrame(data, columns=columns)

# Sort by function containing known longevity keywords (simple keyword-based approach)
longevity_keywords = ["longevity", "mTOR", "lifespan", "aging", "nutrient sensing", "Alzheimer", "oxidant", "mevalonate"]
df['Priority'] = df['Function'].str.contains('|'.join(longevity_keywords), case=False)
df_sorted = pd.concat([df[df.Priority], df[~df.Priority]]).drop(columns="Priority")

# Save to high-quality PNG image
fig, ax = plt.subplots(figsize=(20, 10))
ax.axis('off')
table = Table(ax, bbox=[0, 0, 1, 1])

n_rows, n_cols = df_sorted.shape
widths = [0.08, 0.08, 0.08, 0.76]
cell_text = [columns] + df_sorted.values.tolist()

for i in range(len(cell_text)):
    for j in range(len(cell_text[0])):
        cell = table.add_cell(i, j, widths[j], 1 / (n_rows + 1), text=cell_text[i][j], loc='left')
        if i == 0:
            cell.set_fontsize(12)
            cell.set_text_props(weight='bold', color='white')
            cell.set_facecolor('#4F81BD')
        elif df_sorted.iloc[i-1]["Function"].lower().find("longevity") != -1 or df_sorted.iloc[i-1]["Function"].lower().find("mTOR") != -1:
            cell.set_facecolor('#DDEBF7')
        else:
            cell.set_facecolor('#FFFFFF')

ax.add_table(table)
png_path = "./Longevity_Table.png"
plt.savefig(png_path, dpi=600, bbox_inches='tight')

# Also generate a PDF version
pdf_path = "./longevity_Table.pdf"
doc = SimpleDocTemplate(pdf_path, pagesize=letter)
styles = getSampleStyleSheet()
pdf_table_data = [columns] + df_sorted.values.tolist()

formatted_data = [[Paragraph(str(cell), styles['Normal']) for cell in row] for row in pdf_table_data]

pdf_table = PDFTable(formatted_data, repeatRows=1)
pdf_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#4F81BD")),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, -1), 9),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.whitesmoke, colors.lightgrey]),
    ('GRID', (0, 0), (-1, -1), 0.25, colors.grey),
]))

doc.build([pdf_table])

png_path, pdf_path

