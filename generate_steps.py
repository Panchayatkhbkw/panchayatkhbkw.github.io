import os

images_dir = r"c:\Users\Lenovo Desktop\Documents\Coddes\Monity X Project\News Portall\process explain page\images"
files = sorted([f for f in os.listdir(images_dir) if f.lower().endswith(('.jpg', '.png', '.jpeg'))])

content = ""
for i, filename in enumerate(files, 1):
    # Extract hint
    # Format: Screenshot_YYYYMMDD_HHMMSS_Hint.jpg
    # or Screenshot_YYYYMMDD_HHMMSS.jpg
    name_parts = filename.replace('.jpg', '').replace('.jpeg', '').split('_')
    
    title = f"Step {i}"
    description = ""
    
    if len(name_parts) >= 4:
        hint = " ".join(name_parts[3:]).strip()
        if hint:
            title = hint
            description = f"Perform the action shown in the {hint} screen."
    else:
        description = "Follow the instruction on the screen."

    if not description:
         description = "Proceed as shown."

    content += f"""
        <!-- ===============================
             STEP {i}
        ================================ -->
        <section class="step">
            <div class="step-content">
                <div class="step-header">
                    <div class="step-number">Step {i}</div>
                    <div class="step-title">{title}</div>
                </div>

                <p class="step-description">
                    {description}
                </p>
            </div>

            <div class="step-image">
                <div class="phone-frame">
                    <img src="images/{filename}" alt="Step {i} Screenshot">
                </div>
            </div>
        </section>
    """

# Read index.html
with open("index.html", "r", encoding="utf-8") as f:
    template = f.read()

# Find split points
# We want to replace everything after </header> and before <footer>
header_end_tag = "</header>"
footer_start_tag = "<footer>"

start_idx = template.find(header_end_tag)
end_idx = template.find(footer_start_tag)

if start_idx != -1 and end_idx != -1:
    # Adjust start_idx to be after the tag
    start_idx += len(header_end_tag)
    
    new_html = template[:start_idx] + "\n\n" + content + "\n        " + template[end_idx:]
    
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(new_html)
    print("Successfully updated index.html")
else:
    print(f"Markers not found! Start: {start_idx}, End: {end_idx}")
