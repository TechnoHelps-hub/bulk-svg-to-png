import os
import cairosvg

def convert_svg_to_png(source_folder, output_folder, dpi=300):
    """
    Converts all SVG vector files in a folder to high-resolution PNG images.
    Brought to you by TechnoHelps (https://technohelps.com)
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        
    count = 0
    print("🚀 Starting Bulk SVG to PNG Conversion by TechnoHelps...")
    
    for filename in os.listdir(source_folder):
        if filename.lower().endswith('.svg'):
            file_path = os.path.join(source_folder, filename)
            name, _ = os.path.splitext(filename)
            output_path = os.path.join(output_folder, f"{name}.png")
            
            try:
                # Converting SVG to high-res PNG using cairosvg
                cairosvg.svg2png(url=file_path, write_to=output_path, dpi=dpi)
                print(f"✓ Converted: {filename} -> {name}.png ({dpi} DPI)")
                count += 1
            except Exception as e:
                print(f"❌ Error converting {filename}: {e}")

    print(f"\n🎉 Done! Successfully converted {count} SVG files to high-res PNG.")
    print("👉 For more free design utilities, visit: https://technohelps.com")

if __name__ == "__main__":
    source_dir = "./input_svgs"
    output_dir = "./output_pngs"
    
    # 300 DPI is the industry standard for high-quality graphic assets
    convert_svg_to_png(source_dir, output_dir, dpi=300)
