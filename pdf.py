import json
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.units import inch

# JSON template (as above)
resume_json_str = r'''
{
  "document": {
    "page": {
      "size": "letter",
      "margin": { "top": 50, "bottom": 50, "left": 50, "right": 50 },
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
          "lineSpacing": 1.2
        }
      },
      {
        "type": "subheader",
        "text": "+91 9319475235 | rdilshad3559@gmail.com | linkedin.com/in/dilshad-ansari-dev | github.com/lytcode404",
        "style": {
          "fontSize": 10,
          "alignment": "center",
          "lineSpacing": 1.2
        }
      },
      { "type": "spacer", "size": 20 },
      {
        "type": "section",
        "title": "Education",
        "style": {
          "fontSize": 12,
          "bold": true,
          "alignment": "left",
          "marginBottom": 5
        }
      },
      {
        "type": "entry",
        "title": "Netaji Subhash University of Technology, Delhi",
        "subtitle": "Bachelor’s Degree in Electronics and Communication Engineering – (CGPA –7.6)  |  Nov 2022 – Present",
        "description": "in Artificial Intelligence and Machine Learning",
        "style": {
          "fontSize": 10,
          "alignment": "left",
          "lineSpacing": 1.2
        }
      },
      {
        "type": "entry",
        "title": "Rajkiya Pratibha Vikas Vidyalaya, Dwarka Sec 5 Delhi",
        "subtitle": "Higher Secondary Education - (Class 12 - 91.6%)",
        "description": "May 2020 – May 2021",
        "style": {
          "fontSize": 10,
          "alignment": "left",
          "lineSpacing": 1.2
        }
      },
      { "type": "spacer", "size": 10 },
      {
        "type": "section",
        "title": "Technical Skills",
        "style": {
          "fontSize": 12,
          "bold": true,
          "alignment": "left",
          "marginBottom": 5
        }
      },
      {
        "type": "text",
        "text": "Languages: Python, Javascript, Django, Flask, Cython, JavaScript, Go, Shell Scripting (Bash), C/C++, SQL (Postgres), HTML/CSS",
        "style": {
          "fontSize": 10,
          "alignment": "left",
          "lineSpacing": 1.2
        }
      },
      {
        "type": "text",
        "text": "Frameworks: React, Next.js, Node.js, Express Js, WordPress, FastAPI",
        "style": {
          "fontSize": 10,
          "alignment": "left",
          "lineSpacing": 1.2
        }
      },
      {
        "type": "text",
        "text": "Developer Tools: Git, Docker, Google Cloud Platform, AWS, VS Code, Jupyter Notebook, Google Colab",
        "style": {
          "fontSize": 10,
          "alignment": "left",
          "lineSpacing": 1.2
        }
      },
      {
        "type": "text",
        "text": "Libraries: pandas, NumPy, Matplotlib, Keras, Tensorflow, Sci-kit Learn",
        "style": {
          "fontSize": 10,
          "alignment": "left",
          "lineSpacing": 1.2
        }
      },
      { "type": "spacer", "size": 10 },
      {
        "type": "section",
        "title": "Experience",
        "style": {
          "fontSize": 12,
          "bold": true,
          "alignment": "left",
          "marginBottom": 5
        }
      },
      {
        "type": "entry",
        "title": "Full Stack Developer  |  Oct 2024 - Dec 2024",
        "subtitle": "E-commerce Website (adiprabha.com) Delhi",
        "bullets": [
          "Developed and deployed a fully responsive e-commerce platform using ReachJs, Nextjs, and Tailwind CSS, ensuring fast load times and a seamless user experience across 98% of devices.",
          "Engineered a secure backend with Firestore DB and Nodejs, handling more than 1,000 product records, while integrating Google Authentication for smooth user sign-in processes.",
          "Created an intuitive Admin panel, enabling administrators to upload, edit, and delete products, enhancing management efficiency by 40% and providing visually engaging designs with Tailwind CSS."
        ],
        "style": {
          "fontSize": 10,
          "alignment": "left",
          "lineSpacing": 1.2
        }
      },
      {
        "type": "entry",
        "title": "Full Stack Next.js Developer  |  Feb 2024 - May 2024",
        "subtitle": "ARW Tours and Travels (arwtoursandtravelsgoa.com) Delhi",
        "bullets": [
          "Designed a travel booking platform with trip planning tools, destination guides, sightseeing suggestions, and hotel reservations, increasing user engagement by 25% and supporting over 10,000 bookings.",
          "Optimized backend and APIs, reducing server costs and improving website performance by 40% through code refactoring, improved caching, and streamlined database queries.",
          "Surpassed industry benchmarks against Tripplanner.in and Templemitra.com, achieving a 20% growth in the user base and strengthening market presence through targeted outreach."
        ],
        "style": {
          "fontSize": 10,
          "alignment": "left",
          "lineSpacing": 1.2
        }
      },
      {
        "type": "entry",
        "title": "Full Stack MERN Developer  |  Aug 2023 – Jan 2024",
        "subtitle": "Phoenix Ventures (phoenixventures.me) Delhi",
        "bullets": [
          "Engineered an advanced admin panel for business enlistment on Paronama, reducing backend integration time by 40% and increasing user-business interactions by 25%.",
          "Developed a scalable Node.js, Express.Js backend, improving response times by 30% through optimized Firebase NoSQL queries and efficient API design.",
          "Enhanced website security by integrating advanced authentication mechanisms, improving access control by 40% and ensuring robust data protection."
        ],
        "style": {
          "fontSize": 10,
          "alignment": "left",
          "lineSpacing": 1.2
        }
      },
      { "type": "spacer", "size": 10 },
      {
        "type": "section",
        "title": "Projects",
        "style": {
          "fontSize": 12,
          "bold": true,
          "alignment": "left",
          "marginBottom": 5
        }
      },
      {
        "type": "entry",
        "title": "Shop Smart Analyser | React.js, Node.js, Python, Chrome Inbuilt APIs  |  Apr 2024",
        "bullets": [
          "Achieved 1st place, outperforming thousands of competing teams, and secured a 12 lakh prize pool at AMDOCS MOKSHA INNOVISION.",
          "Implemented Chrome APIs to analyze over 100 Flipkart product listings with reduced server load and an average response time under 200 ms."
        ],
        "style": {
          "fontSize": 10,
          "alignment": "left",
          "lineSpacing": 1.2
        }
      },
      {
        "type": "entry",
        "title": "Crypto Bubbles | Next.js, Node.js, TailwindCSS, Flask, Python, Vercel  |  May 2018 – May 2020",
        "bullets": [
          "Created a visually intuitive web application for displaying cryptocurrency data through dynamically floating cloudy bubbles and over 10 parameters for in-depth cryptocurrency analysis.",
          "Ranked in the top 10 at Adobe DevCraft hosted at DTU for innovative web development."
        ],
        "style": {
          "fontSize": 10,
          "alignment": "left",
          "lineSpacing": 1.2
        }
      },
      { "type": "spacer", "size": 20 },
      {
        "type": "footer",
        "text": "mailto:x@x.com | https://linkedin.com/in/dilshad-ansari-dev | https://github.com/...",
        "style": {
          "fontSize": 10,
          "alignment": "center",
          "lineSpacing": 1.2
        }
      }
    ]
  }
}
'''


def create_paragraph_style(name, style_data, default_font="Helvetica"):
    from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
    alignment_map = {"left": TA_LEFT, "center": TA_CENTER, "right": TA_RIGHT}
    fontSize = style_data.get("fontSize", 10)
    ps = ParagraphStyle(
        name=name,
        fontName=default_font,
        fontSize=fontSize,
        leading=fontSize * style_data.get("lineSpacing", 1.2),
        alignment=alignment_map.get(style_data.get(
            "alignment", "left").lower(), TA_LEFT)
    )
    if style_data.get("bold", False):
        ps.fontName = default_font + "-Bold"
    if "marginBottom" in style_data:
        ps.spaceAfter = style_data["marginBottom"]
    return ps


def process_element(element, default_font):
    flowables = []
    style_data = element.get("style", {})
    ps = create_paragraph_style("custom", style_data, default_font)
    elem_type = element["type"]

    if elem_type in ["header", "subheader", "section", "text", "footer"]:
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
    page_size_str = document.get("page", {}).get("size", "letter").lower()
    page_size = letter if page_size_str == "letter" else A4
    margins = document.get("page", {}).get(
        "margin", {"top": 50, "bottom": 50, "left": 50, "right": 50})
    default_font = document.get("page", {}).get("defaultFont", "Helvetica")

    doc = SimpleDocTemplate(
        output_filename,
        pagesize=page_size,
        rightMargin=margins.get("right", 50),
        leftMargin=margins.get("left", 50),
        topMargin=margins.get("top", 50),
        bottomMargin=margins.get("bottom", 50)
    )

    flowables = []
    for element in document.get("elements", []):
        flowables.extend(process_element(element, default_font))

    doc.build(flowables)
    print(f"PDF generated successfully: {output_filename}")


if __name__ == "__main__":
    build_pdf_from_json(
        resume_json_str, output_filename="Dilshad_Resume_CloudOps.pdf")
