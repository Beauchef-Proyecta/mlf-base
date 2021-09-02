# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 02:41:58 2021

@author: Ulises
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def forward_kinematics(q0, q1, q2):
    # Largos de los links
    a1 = 55
    a2 = 39
    a3 = 135
    a4 = 147
    a5 = 66.3
    # Grados a radianes para los joints
    q0 = q0 * np.pi / 180
    q1 = q1 * np.pi / 180
    q2 = q2 * np.pi / 180

    # Tranformadas
    Tz_a1 = [1, 0, 0, 0], \
            [0, 1, 0, 0], \
            [0, 0, 1, a1], \
            [0, 0, 0, 1]

    Rz_q0 = [np.cos(q0), -np.sin(q0), 0, 0], \
            [np.sin(q0), np.cos(q0), 0, 0], \
            [0, 0, 1, 0], \
            [0, 0, 0, 1]

    Tz_a2 = [1, 0, 0, 0], \
            [0, 1, 0, 0], \
            [0, 0, 1, a2], \
            [0, 0, 0, 1]

    Ry_q1 = [np.cos(q1), 0, -np.sin(q1), 0], \
            [0, 1, 0, 0], \
            [np.sin(q1), 0, np.cos(q1), 0], \
            [0, 0, 0, 1]

    Tz_a3 = [1, 0, 0, 0], \
            [0, 1, 0, 0], \
            [0, 0, 1, a3], \
            [0, 0, 0, 1]

    Ry_piq2 = [np.cos(-(np.pi - q2)), 0, np.sin(-(np.pi - q2)), 0], \
              [0, 1, 0, 0], \
              [-np.sin(-(np.pi - q2)), 0, np.cos(-(np.pi - q2)), 0], \
              [0, 0, 0, 1]

    Tz_a4 = [1, 0, 0, 0], \
            [0, 1, 0, 0], \
            [0, 0, 1, a4], \
            [0, 0, 0, 1]

    Ry_q1q2 = [np.cos(np.pi - (q1 + q2)), 0, -np.sin(np.pi - (q1 + q2)), 0], \
              [0, 1, 0, 0], \
              [np.sin(np.pi - (q1 + q2)), 0, np.cos(np.pi - (q1 + q2)), 0], \
              [0, 0, 0, 1]

    Tz_a5 = [1, 0, 0, 0], \
            [0, 1, 0, 0], \
            [0, 0, 1, a5], \
            [0, 0, 0, 1]

    # wrap de matrices para multiplicar
    # H=[Tz_a1,Rz_q0,Tz_a2,Ry_q1,Tz_a3, Ry_piq2, Tz_a4,Ry_q1q2,Tz_a5]
    # H_tf= linalg.multi_dot(Tz_a1, Rz_q0, Tz_a2, Ry_q1, Tz_a3, Ry_piq2, Tz_a4, Ry_q1q2, Tz_a5)

    # Recuperamos posiciones de los joints para plotear
    base_tf = [Tz_a1, Rz_q0, Tz_a2]
    base_matrix = np.linalg.multi_dot(base_tf)
    x_base = np.round(base_matrix[0, 3], 3)
    y_base = np.round(base_matrix[1, 3], 3)
    z_base = np.round(base_matrix[2, 3], 3)

    l1_tf = [Tz_a1, Rz_q0, Tz_a2, Ry_q1, Tz_a3]
    l1_matrix = np.linalg.multi_dot(l1_tf)
    x_l1 = np.round(l1_matrix[0, 3], 3)
    y_l1 = np.round(l1_matrix[1, 3], 3)
    z_l1 = np.round(l1_matrix[2, 3], 3)

   #l2_tf = [Tz_a1, Rz_q0, Tz_a2, Ry_q1, Tz_a3, Ry_piq2, Tz_a4, Tz_a5]
    #sin gripper
    l2_tf = [Tz_a1, Rz_q0, Tz_a2, Ry_q1, Tz_a3, Ry_piq2, Tz_a4]
    l2_matrix = np.linalg.multi_dot(l2_tf)
    x_l2 = np.round(l2_matrix[0, 3], 3)
    y_l2 = np.round(l2_matrix[1, 3], 3)
    z_l2 = np.round(l2_matrix[2, 3], 3)

    link_positions = np.array([x_base, y_base, z_base, x_l1, y_l1, z_l1, x_l2, y_l2, z_l2])
    # return H_tf
    return link_positions


pose_pedida = forward_kinematics(180, 0, 90)

X_pos = [pose_pedida[0] , pose_pedida[3] , pose_pedida[6]]
Y_pos = [pose_pedida[1] , pose_pedida[4] , pose_pedida[7]]
Z_pos = [pose_pedida[2] , pose_pedida[5] , pose_pedida[8]]


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(0, 0, 0, zdir='z', s=30)
ax.plot([0,X_pos[0]],[0,Y_pos[0]],[0,Z_pos[0]])
ax.plot([X_pos[0],X_pos[1]],[Y_pos[0],Y_pos[1]],[Z_pos[0],Z_pos[1]])
ax.plot([X_pos[1],X_pos[2]],[Y_pos[1],Y_pos[2]],[Z_pos[1],Z_pos[2]])
ax.scatter(X_pos, Y_pos, Z_pos, zdir='z', s=20)

ax.set_ylabel('Y')
ax.set_xlabel('X')
ax.set_zlabel('Z')
plt.xlim(0, 300)
plt.ylim(-300, 300)


plt.show()