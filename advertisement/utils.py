from xml.etree.ElementTree import Element, tostring
from xml.dom import minidom


def convert_xml(obj):
    """
    Convert data into xml format
    """
    root = Element("Advertisement")

    fields = {
        "add_id": str(obj.add_id),
        "title": obj.title or "",
        "image_url": obj.image_url or "",
        "website": obj.website or "",
        "description": obj.description or "",
        "company": obj.company or "",
        "button_text": obj.button_text or "",
    }

    for key, value in fields.items():
        child = Element(key)
        child.text = value
        root.append(child)

    raw_xml = tostring(root, encoding="unicode")
    pretty_xml = minidom.parseString(raw_xml).toprettyxml(indent="  ")
    return pretty_xml
