from pathlib import Path
from streamlit.components.v1 import declare_component

_RELEASE = True

if not _RELEASE:
    _component_func = declare_component("streamlit_disqus", url="http://localhost:3001")
else:
    _component_path = (Path(__file__).parent/"frontend"/"build").resolve()
    _component_func = declare_component("streamlit_disqus", path=_component_path)


def st_disqus(
    shortname,
    url=None,
    identifier=None,
    title=None,
    category_id=None,
    language=None,
    key=None
):
    """Integrate Disqus into your Streamlit application.
    
    Parameters
    ----------
    shortname : str
        The unique identifier for your website as registered on Disqus.
    url : str or None
        A unique URL for each page where Disqus is present.
    identifier : str or None
        A unique identifier for each page where Disqus is present.
    title : str or None
        A unique title for each page where Disqus is present.
    category_id : str or None
        An ID for the category that will to be associated with the
        current page.
    language : str or None
        A parameter for dynamically specifying the language for
        multilingual websites.
    key : str or None
        An optional string to use as the unique key for the widget.
        If this is omitted, a key will be generated for the widget
        based on its content. Multiple widgets of the same type may
        not share the same key.

    """
    _component_func(
        shortname=shortname,
        url=url,
        identifier=identifier,
        title=title,
        categoryID=category_id,
        language=language,
        key=key,
        default=None
    )
