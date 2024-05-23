# H - uint16, h - int16, I - uint32, i - int32, c - char

class Thing:
    __slots__ = [
        'pos',
        'angle',
        'type',
        'flags'
    ]

class Seg:
    __slots__ = [
        'start_vertex_id',
        'end_vertex_id',
        'angle',
        'lindedef_id',
        'direction',
        'offset',
    ]

class SubSector:
    __slots__ = [
        'seg_count',
        'first_seg_id'
    ]

class Node:
    class BBox:
        __slots__ = ['top', 'bottom', 'left', 'right']

    __slots__ = [
        'x_partition',
        'y_partition',
        'dx_partition',
        'dy_partition',
        'bbox',
        'front_child_id',
        'back_child_id'
    ]
    
    def __init__(self):
        self.bbox = {'front': self.BBox(), 'back': self.BBox()}

class Lindedef:
    # 14 bytes = 2H x 7
    __slots__ = [
        'start_vertex_id',
        'end_vertex_id',
        'flags',
        'line_type',
        'sector_tag',
        'front_sidedef_id',
        'back_sidedef_id'
    ]
