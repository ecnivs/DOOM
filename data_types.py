class TextureMap:
    __slots__ = [
        'name',
        'flags',
        'width',
        'height',
        'column_dir',
        'patch_count',
        'patch_maps',
    ]

class PatchMap:
    __slots__ = [
        'x_offset',
        'y_offset',
        'p_name_index',
        'step_dir',
        'color_map',
    ]

class TextureHeader:
    __slots__ = [
        'texture_count',
        'texture_offset',
        'texture_data_offset',
    ]

class PatchColumn:
    __slots__ = [
        'top_delta',
        'length',
        'padding_pre',
        'data',
        'padding_post'
    ]

class PatchHeader:
    __slots__ = [
        'width',
        'height',
        'left_offset',
        'top_offset',
        'column_offset'
    ]

class Thing:
    __slots__ = [
        'pos',
        'angle',
        'type',
        'flags'
    ]

class Sector:
    __slots__ = [
        'floor_height',
        'ceil_height',
        'floor_texture',
        'ceil_texture',
        'light_level',
        'type',
        'tag'
    ]

class Sidedef:
    __slots__ = [
        'x_offset',
        'y_offset',
        'upper_texture',
        'lower_texture',
        'middle_texture',
        'sector_id',
    ]
    __slots__ += ['sector']

class Seg:
    __slots__ = [
        'start_vertex_id',
        'end_vertex_id',
        'angle',
        'linedef_id',
        'direction',
        'offset',
    ]
    __slots__ += ['start_vertex', 'end_vertex', 'linedef', 'front_sector', 'back_sector']

class Linedef:
    __slots__ = [
        'start_vertex_id',
        'end_vertex_id',
        'flags',
        'line_type',
        'sector_tag',
        'front_sidedef_id',
        'back_sidedef_id'
    ]
    __slots__ += ['front_sidedef', 'back_sidedef']

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
        'bbox',  # 8h
        'front_child_id',
        'back_child_id',
    ]
    def __init__(self):
        self.bbox = {'front': self.BBox(), 'back': self.BBox()}
