__all__ = [
    'middle_default',
]


load_middle_history = None

if load_middle_history is None:
    from pye.content.content_middle.default import middle_default
    middle_default = middle_default()
else:
    from pye.content.content_middle.default import middle_default
    middle_default = middle_default()
