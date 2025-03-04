import json
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.units import inch
from reportlab.lib import colors

# Improved JSON template with enhanced styling and improved fonts/colors
resume_json_str = r'''
{
  "document": {
    "page": {
      "size": "letter",
      "margin": { "top": 10, "bottom": 10, "left": 10, "right": 10 },
      "defaultFont": "Helvetica"
    },
    "elements": [
      {
        "type": "header",
        "text": "Dilshad Ansari",
        "style": {
          "fontSize": 24,
          "bold": true,
          "alignment": "center",
          "lineSpacing": 1.1,
          "color": "#2c3e50"
        }
      },
      {
        "type": "subheader",
        "text": "+91 9319475235 | rdilshad3559@gmail.com | linkedin.com/in/dilshad-ansari-dev | github.com/lytcode404",
        "style": {
          "fontSize": 11,
          "alignment": "center",
          "lineSpacing": 1.3,
          "color": "#7f8c8d"
        }
      },
      { "type": "spacer", "size": 20 },
      {
        "type": "section",
        "title": "Education",
        "style": {
          "fontSize": 13,
          "bold": true,
          "alignment": "left",
          "marginBottom": 2,
          "color": "#34495e"
        }
      },
      {
        "type": "entry",
        "title": "Netaji Subhash University of Technology, Delhi",
        "subtitle": "Bachelor’s Degree in Electronics and Communication Engineering – (CGPA – 7.6) | Nov 2022 – Present",
        "description": "Specialization in Artificial Intelligence and Machine Learning",
        "style": {
          "fontSize": 11,
          "alignment": "left",
          "lineSpacing": 1.3,
          "color": "#2c3e50"
        }
      },
      {
        "type": "entry",
        "title": "Rajkiya Pratibha Vikas Vidyalaya, Dwarka Sec 5 Delhi",
        "subtitle": "Higher Secondary Education - (Class 12 - 91.6%)",
        "description": "May 2020 – May 2021",
        "style": {
          "fontSize": 11,
          "alignment": "left",
          "lineSpacing": 1.3,
          "color": "#2c3e50"
        }
      },
      { "type": "spacer", "size": 15 },
      {
        "type": "section",
        "title": "Technical Skills",
        "style": {
          "fontSize": 13,
          "bold": true,
          "alignment": "left",
          "marginBottom": 2,
          "color": "#34495e"
        }
      },
      {
        "type": "text",
        "text": "Languages: Python, Javascript, Django, Flask, Cython, JavaScript, Go, Shell Scripting (Bash), C/C++, SQL (Postgres), HTML/CSS",
        "style": {
          "fontSize": 11,
          "alignment": "left",
          "lineSpacing": 1.3,
          "color": "#2c3e50"
        }
      },
      {
        "type": "text",
        "text": "Frameworks: React, Next.js, Node.js, Express Js, WordPress, FastAPI",
        "style": {
          "fontSize": 11,
          "alignment": "left",
          "lineSpacing": 1.3,
          "color": "#2c3e50"
        }
      },
      {
        "type": "text",
        "text": "Developer Tools: Git, Docker, Google Cloud Platform, AWS, VS Code, Jupyter Notebook, Google Colab",
        "style": {
          "fontSize": 11,
          "alignment": "left",
          "lineSpacing": 1.3,
          "color": "#2c3e50"
        }
      },
      {
        "type": "text",
        "text": "Libraries: pandas, NumPy, Matplotlib, Keras, Tensorflow, Sci-kit Learn",
        "style": {
          "fontSize": 11,
          "alignment": "left",
          "lineSpacing": 1.3,
          "color": "#2c3e50"
        }
      },
      { "type": "spacer", "size": 15 },
      {
        "type": "section",
        "title": "Experience",
        "style": {
          "fontSize": 13,
          "bold": true,
          "alignment": "left",
          "marginBottom": 2,
          "color": "#34495e"
        }
      },
      {
        "type": "entry",
        "title": "Full Stack Developer | Oct 2024 - Dec 2024",
        "subtitle": "E-commerce Website (adiprabha.com) Delhi",
        "bullets": [
          "Developed and deployed a fully responsive e-commerce platform using ReachJs, Nextjs, and Tailwind CSS, ensuring fast load times and a seamless user experience.",
          "Engineered a secure backend with Firestore DB and Nodejs, handling over 1,000 product records with integrated Google Authentication.",
          "Created an intuitive Admin panel for product management, enhancing efficiency by 40% with visually engaging designs."
        ],
        "style": {
          "fontSize": 11,
          "alignment": "left",
          "lineSpacing": 1.3,
          "color": "#2c3e50"
        }
      },
      {
        "type": "entry",
        "title": "Full Stack Next.js Developer | Feb 2024 - May 2024",
        "subtitle": "ARW Tours and Travels (arwtoursandtravelsgoa.com) Delhi",
        "bullets": [
          "Designed a travel booking platform with trip planning tools, destination guides, and hotel reservations, increasing user engagement by 25%.",
          "Optimized backend and APIs, reducing server costs and improving website performance by 40% through refactoring and caching.",
          "Achieved a 20% growth in the user base through targeted outreach and market presence enhancement."
        ],
        "style": {
          "fontSize": 11,
          "alignment": "left",
          "lineSpacing": 1.3,
          "color": "#2c3e50"
        }
      },
      {
        "type": "entry",
        "title": "Full Stack MERN Developer | Aug 2023 – Jan 2024",
        "subtitle": "Phoenix Ventures (phoenixventures.me) Delhi",
        "bullets": [
          "Engineered an advanced admin panel for business enlistment on Paronama, reducing backend integration time by 40%.",
          "Developed a scalable Node.js, Express.Js backend, improving response times by 30% with optimized Firebase NoSQL queries.",
          "Enhanced website security with advanced authentication, improving access control by 40%."
        ],
        "style": {
          "fontSize": 11,
          "alignment": "left",
          "lineSpacing": 1.3,
          "color": "#2c3e50"
        }
      },
      { "type": "spacer", "size": 15 },
      {
        "type": "section",
        "title": "Projects",
        "style": {
          "fontSize": 13,
          "bold": true,
          "alignment": "left",
          "marginBottom": 8,
          "color": "#34495e"
        }
      },
      {
        "type": "entry",
        "title": "Shop Smart Analyser | React.js, Node.js, Python, Chrome APIs | Apr 2024",
        "bullets": [
          "Achieved 1st place at AMDOCS MOKSHA INNOVISION with a prize pool of 12 lakh.",
          "Implemented Chrome APIs to analyze over 100 Flipkart product listings, reducing server load with an average response time under 200 ms."
        ],
        "style": {
          "fontSize": 11,
          "alignment": "left",
          "lineSpacing": 1.3,
          "color": "#2c3e50"
        }
      },
      {
        "type": "entry",
        "title": "Crypto Bubbles | Next.js, Node.js, TailwindCSS, Flask, Python, Vercel | May 2018 – May 2020",
        "bullets": [
          "Developed a web application for cryptocurrency data using dynamically floating cloudy bubbles and multi-parameter analysis.",
          "Ranked in the top 10 at Adobe DevCraft for innovative web development."
        ],
        "style": {
          "fontSize": 11,
          "alignment": "left",
          "lineSpacing": 1.3,
          "color": "#2c3e50"
        }
      },
      { "type": "spacer", "size": 20 },
      {
        "type": "footer",
        "style": {
          "fontSize": 10,
          "alignment": "center",
          "lineSpacing": 1.3,
          "color": "#7f8c8d"
        }
      }
    ]
  }
}
'''


def create_paragraph_style(name, style_data, default_font="Helvetica"):
    alignment_map = {"left": TA_LEFT, "center": TA_CENTER, "right": TA_RIGHT}
    fontSize = style_data.get("fontSize", 11)
    lineSpacing = style_data.get("lineSpacing", 1.3)
    ps = ParagraphStyle(
        name=name,
        fontName=default_font,
        fontSize=fontSize,
        leading=fontSize * lineSpacing,
        alignment=alignment_map.get(style_data.get(
            "alignment", "left").lower(), TA_LEFT),
        spaceBefore=style_data.get("spaceBefore", 0)
    )
    if style_data.get("bold", False):
        ps.fontName = default_font + "-Bold"
    if "marginBottom" in style_data:
        ps.spaceAfter = style_data["marginBottom"]
    if style_data.get("color"):
        ps.textColor = colors.HexColor(style_data["color"])
    return ps


def process_element(element, default_font):
    flowables = []
    style_data = element.get("style", {})
    ps = create_paragraph_style("custom", style_data, default_font)
    elem_type = element["type"]

    if elem_type in ["header", "subheader", "section", "text", "footer"]:
        # Use either "text" or "title" for the main content.
        text = element.get("text") or element.get("title") or ""
        flowables.append(Paragraph(text, ps))
    elif elem_type == "spacer":
        flowables.append(Spacer(1, element.get("size", 10)))
    elif elem_type == "entry":
        parts = []
        title = element.get("title", "")
        subtitle = element.get("subtitle", "")
        description = element.get("description", "")
        if title:
            parts.append(f"<b>{title}</b>")
        if subtitle:
            parts.append(f"<i>{subtitle}</i>")
        if description:
            parts.append(description)
        entry_text = "<br/>".join(parts)
        if entry_text:
            flowables.append(Paragraph(entry_text, ps))
        for bullet in element.get("bullets", []):
            bullet_text = f"&#8226; {bullet}"
            bullet_ps = create_paragraph_style(
                "bullet", {**style_data, "alignment": "left"}, default_font)
            bullet_ps.leftIndent = 15
            flowables.append(Paragraph(bullet_text, bullet_ps))
    return flowables


def build_pdf_from_json(resume_json, output_filename="Dilshad_Resume_CloudOps.pdf"):
    data = json.loads(resume_json)
    document = data["document"]

    # Adjust page size and margins
    page_size_str = document.get("page", {}).get("size", "letter").lower()
    page_size = letter if page_size_str == "letter" else A4
    margins = document.get("page", {}).get(
        "margin", {"top": 10, "bottom": 10, "left": 10, "right": 10})

    # Adjust font sizes and styles
    for element in document.get("elements", []):
        style_data = element.get("style", {})
        if "fontSize" in style_data:
            # Limit font size to 11 points
            style_data["fontSize"] = min(style_data["fontSize"], 11)
        if "lineSpacing" in style_data:
            style_data["lineSpacing"] = min(
                style_data["lineSpacing"], 1.2)  # Adjust line spacing

    doc = SimpleDocTemplate(
        output_filename,
        pagesize=page_size,
        rightMargin=margins.get("right", 10),
        leftMargin=margins.get("left", 10),
        topMargin=margins.get("top", 10),
        bottomMargin=margins.get("bottom", 10)
    )

    flowables = []
    for element in document.get("elements", []):
        flowables.extend(process_element(element, "Helvetica"))

    doc.build(flowables)
    print(f"PDF generated successfully: {output_filename}")


if __name__ == "__main__":
    build_pdf_from_json(
        resume_json_str, output_filename="Dilshad_Resume_CloudOps.pdf")
