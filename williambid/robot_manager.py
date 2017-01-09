from williambid.models import Robot as DBRobot, Subasta
from williambid.robots import Robot as PythonRobot
from williambid.service_layer import crear_usuario_para_robot
from williambid.models import Subasta


class RobotManager:

    def __init__(self):
        # cantidad de robots a crear en la base de datos
        self.cantidad_robot = 5
        self.robots_asignados = {}

    # esta funcion tiene cuenta que un robot, no se encuentre trabajando en 2 o mas subastas al mismo tiempo
    def asignar_robot_a_subasta(self, subasta_id):
        robots_with_subasta = DBRobot.objects.filter(subasta_id=subasta_id).first()
        # si ya esta subasta tiene un robot, salimos
        if robots_with_subasta:
            return
        # se obtienen los robots desde la base de datos
        if len(DBRobot.objects.filter(subasta__id__isnull=True).all()) < 1:
            self.crear_usuarios_robots()
        db_candidate_robot = DBRobot.objects.filter(subasta__id__isnull=True).first()
        print "Asignando robot a subasta %s" % str(subasta_id)
        db_candidate_robot.subasta = Subasta.objects.get(id=subasta_id)
        db_candidate_robot.save(force_update=True)
        # creamos el robot script
        robot_python = PythonRobot(db_candidate_robot.id_robot, db_candidate_robot.usuario.username, subasta_id,
                                   db_candidate_robot.usuario.id)
        # guardar el Thread en este dict para ulteriormente parar el hilo
        self.robots_asignados[db_candidate_robot.id_robot] = robot_python
        return robot_python

    # asignar_robot_a_subasta = staticmethod(asignar_robot_a_subasta)

    def liberar_robots_de_subastas_terminadas(self):
        print "Attempting release robots ..."
        robots_with_subastas = DBRobot.objects.filter(subasta__estado=Subasta.FINISHED).all()
        for robot in robots_with_subastas:
            robot.subasta = None
            robot.save(force_update=True)
            print "Robots asiganados %s" % self.robots_asignados
            if robot.id_robot in self.robots_asignados:
                print "Killing ThreadScript %s" % robot.id_robot
                thread_script = self.robots_asignados[robot.id_robot]
                if thread_script.isAlive():
                    thread_script.terminate()
                    thread_script.join()

    def crear_usuarios_robots(self):
        robots_db = DBRobot.objects.all()
        # si no hay suficientes robots
        if (len(robots_db) < self.cantidad_robot):
            user_robot = crear_usuario_para_robot()
            print "Creando Usuario Robot: %s" % user_robot.username

    # crear_usuarios_robots = staticmethod(crear_usuarios_robots)
