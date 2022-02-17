from entity import *


def SimulationCube():
    boxTrans = Transform3(PosRotScale3(
        Vector3(0, 0, 0), Quaternion(), Vector3(1, 1, 1)), [], Transform3Master.Master)
    Box = Entity(boxTrans, [MeshRenderer(Mesh.Cube)])
    Pyramid = Entity(Transform3(PosRotScale3(Vector3.up * .5, Quaternion(),
                                             Vector3.one * .5), [], boxTrans), [MeshRenderer(Mesh.Pyramid)])
    selectedEntity = Pyramid


def SimulationCoaster(track):
    Ground = Entity(Transform3(PosRotScale3(Vector3(0, 0, -10))),
                    [MeshRenderer(Mesh.Ground, Color.green, Color.darkGreen)])
    Ground.transform.localPosRotScale3.scale = Vector3.one * 10
    # speedVectorRenderer = VectorRenderer()
    accelerationVectorRenderer = VectorRenderer(Color.blue, .1)
    # gForceVectorRenderer = VectorRenderer(Color.red, 2)
    trackPos = Vector3(0, 0, -10)

    Track01 = Entity(Transform3(PosRotScale3(
        trackPos, Quaternion(), Vector3(1, 1, 1)), [], Transform3Master.Master), [MeshRenderer(TrackMesh(track))])
    Cart = Entity(
        Transform3(PosRotScale3(trackPos+track.start, Quaternion(),
                                Vector3(1, 1, 1)), [], Transform3Master.Master),
        [MeshRenderer(Mesh.Cart, Color.red, Color.orange), TrackBody(track, accelerationVectorRenderer, trackPos), accelerationVectorRenderer])
    selectedEntity = Cart
    #Transform3Master.Master.localPosRotScale3.position.z = -25


MainCamera = Entity(Transform3(PosRotScale3(Vector3(0, 0, 0))), [Camera.Main])
selectedEntity = MainCamera
SimulationCoaster(TrackIntegrator.ConstantG)
# SimulationCoaster(Track.CircleLoop)
