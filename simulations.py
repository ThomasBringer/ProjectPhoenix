# A script that run simulations.
# Creates Entities in the scene, specifying their Units, positions and more.

from entity import *

# Sample simulation, with just a cube and a pyramid.


def SimulationCart():
    Cart = Entity(
        Transform3(PosRotScale3(Vector3(0, 0, -1), Quaternion(),
                                Vector3(1, 1, 1)), [], Transform3Master.Master),
        [MeshRenderer(Mesh.Cart, Color.red, Color.orange)])
    selectedEntity = Cart


# Simulation with just cart

def SimulationCube():
    boxTrans = Transform3(PosRotScale3(
        Vector3(0, 0, 0), Quaternion(), Vector3(1, 1, 1)), [], Transform3Master.Master)
    Box = Entity(boxTrans, [MeshRenderer(Mesh.Cube)])
    Pyramid = Entity(Transform3(PosRotScale3(Vector3.up * .5, Quaternion(),
                                             Vector3.one * .5), [], boxTrans), [MeshRenderer(Mesh.Pyramid)])
    selectedEntity = Pyramid

# Roller coaster simulation.


def SimulationCoaster(track):
    Ground = Entity(Transform3(PosRotScale3(Vector3(0, 0, -10))),
                    [MeshRenderer(Mesh.Ground, Color.green, Color.darkGreen)])
    Ground.transform.localPosRotScale3.scale = Vector3.one * 10

    accelerationVectorRenderer = VectorRenderer(Color.blue, .1)

    trackPos = Vector3(0, 0, -10)

    Track01 = Entity(Transform3(PosRotScale3(
        trackPos, Quaternion(), Vector3(1, 1, 1)), [], Transform3Master.Master), [MeshRenderer(TrackMesh(track))])
    Cart = Entity(
        Transform3(PosRotScale3(trackPos+track.start, Quaternion(),
                                Vector3(1, 1, 1)), [], Transform3Master.Master),
        [MeshRenderer(Mesh.Cart, Color.red, Color.orange), TrackBody(track, accelerationVectorRenderer, trackPos), accelerationVectorRenderer])
    selectedEntity = Cart


MainCamera = Entity(Transform3(PosRotScale3(Vector3(0, 0, 0))), [Camera.Main])
selectedEntity = MainCamera

# SimulationCart()
# SimulationCoaster(Track.CircleLoop)
SimulationCoaster(TrackIntegrator.TearLoop)
