# flake8: noqa

if __import__("typing").TYPE_CHECKING:
    # import apis into api package
    from attachmentav.api.attachment_av_api import AttachmentAVApi
    
else:
    from lazy_imports import LazyModule, as_package, load

    load(
        LazyModule(
            *as_package(__file__),
            """# import apis into api package
from attachmentav.api.attachment_av_api import AttachmentAVApi

""",
            name=__name__,
            doc=__doc__,
        )
    )
