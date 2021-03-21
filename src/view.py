
from ase_notebook import AseView, ViewConfig, get_example_atoms, concatenate_svgs
 
# ase_view.config
config = ViewConfig()
ase_view = AseView(config)

ase_view = AseView(
    rotations="45x,45y,45z",
    atom_font_size=16,
    axes_length=30,
    canvas_size=(1000, 400),
    zoom=1.2,
    show_bonds=True
)

def view(structure):
    svgs = []
    for rot in ["45x,45y,45z", "0x", "90x"]:
        ase_view.config.rotations = rot
        ase_view.add_miller_plane(
            1, 0, 0, color="green")
#         1,0,0, color="blue")
        svgs.append(
            ase_view.make_svg(structure, center_in_uc=False)
        )
    return concatenate_svgs(
        svgs, max_columns=3, scale=1, label=True
    )

def view_top(structure):
    ase_view.config.rotations = "0x"
    return ase_view.make_svg(structure,center_in_uc=True)

def view_side(structure):
    ase_view.config.rotations = "90x"
    return ase_view.make_svg(structure,center_in_uc=True)
