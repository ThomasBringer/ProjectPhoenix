from entity import *


def SimulationCube():
    boxTrans = Transform3(PosRotScale3(
        Vector3(0, 0, 0), Quaternion(), Vector3(1, 1, 1)), [], Transform3Master.Master)
    Box = Entity(boxTrans, [MeshRenderer(Mesh.Cube)])
    Pyramid = Entity(Transform3(PosRotScale3(Vector3.up * .5, Quaternion(),
                                             Vector3.one * .5), [], boxTrans), [MeshRenderer(Mesh.Pyramid)])
    selectedEntity = Pyramid


def SimulationCoaster(track):
    Ground = Entity(Transform3(PosRotScale3(Vector3(0, 0, -5))),
                    [MeshRenderer(Mesh.Ground)])
    Ground.transform.localPosRotScale3.scale = Vector3.one * 10
    speedVectorRenderer = VectorRenderer()
    accelerationVectorRenderer = VectorRenderer(Color.orange, .5)
    gForceVectorRenderer = VectorRenderer(Color.red, .5)
    Track01 = Entity(Transform3(PosRotScale3(
        Vector3(0, 0, 0), Quaternion(), Vector3(1, 1, 1)), [], Transform3Master.Master), [MeshRenderer(TrackMesh(track))])
    Cart = Entity(
        Transform3(PosRotScale3(track.start, Quaternion(),
                                Vector3(1, 1, 1)), [], Transform3Master.Master),
        [MeshRenderer(Mesh.Cart), TrackBody(track, speedVectorRenderer, accelerationVectorRenderer, gForceVectorRenderer),
         speedVectorRenderer, accelerationVectorRenderer, gForceVectorRenderer])
    selectedEntity = Cart
    #Transform3Master.Master.localPosRotScale3.position.z = -25


MainCamera = Entity(Transform3(PosRotScale3(Vector3(0, 0, 0))), [Camera.Main])
selectedEntity = MainCamera
SimulationCoaster(Bezier3.DropRoundLoop)

# print("Vector Renderers:", VectorRenderers)
