import bpy
import random
import bpy.props
#from Duplication import *

#Find a Random function that allows python to use float in the range instead of integer for Randomize Grid




class myProperties(bpy.types.PropertyGroup):
    my_bool : bpy.props.BoolProperty(
    name="Enable or Disable",
    description="A simple bool property",
    default = False) 
    
    Tri_equl : bpy.props.BoolProperty(
    name="Enable or Disable",
    description="TriagnleGen Option",
    default = False) 










def add_shapes(context):
    
    bpy.ops.mesh.primitive_cube_add()


def add_sphere(context):
    
    bpy.ops.mesh.primitive_uv_sphere_add()


def deleteObj(context):
    for o in bpy.context.scene.objects:
        if o.select_get() == True:
            bpy.data.objects.remove(o, do_unlink=True)
    



def Duplicate_ObjectZ(context, amount, spacing, Min, bool):
    C = bpy.context
    save = bpy.context.active_object
    
    for i in range (0, amount-1):
        new_obj = bpy.context.active_object.copy()
        new_obj.animation_data_clear()
        print("New: ", new_obj.name)
        
        if bool == True:
            new_obj.location.z += random.randint(int(Min), int(spacing))
        else:
            new_obj.location.z += spacing
        C.collection.objects.link(new_obj)
        context.view_layer.objects.active = new_obj
        Duplicate_ObjectY(context, amount, spacing, Min, bool)
    context.view_layer.objects.active = save


def Duplicate_ObjectY(context, amount, spacing, Min, bool):
    C = bpy.context
    save = bpy.context.active_object
    
    for i in range (0, amount-1):
        new_obj = bpy.context.active_object.copy()
        new_obj.animation_data_clear()
        print("New: ", new_obj.name)
        
        if bool == True:
            new_obj.location.y += random.randint(int(Min), int(spacing))
            
        else:
            new_obj.location.y += spacing
        C.collection.objects.link(new_obj)
        context.view_layer.objects.active = new_obj
    context.view_layer.objects.active = save



def Duplicate_Object(context, amount, spacing, Min, bool):
    C = bpy.context

    if amount == 0 or amount < 0:
        return
    
    if Min >= spacing:
        return
    if bpy.context.active_object == None:
        bpy.props.RemoveProperty(copyObject)
    
    
    for i in range (0, amount):
        new_obj = bpy.context.active_object.copy()
        new_obj.animation_data_clear()
        print("New: ", new_obj.name)
        
        if bool == True:
            new_obj.location.x += random.randint(int(Min), int(spacing))
        else:
            new_obj.location.x += spacing
        C.collection.objects.link(new_obj)
        Duplicate_ObjectZ(context, amount, spacing, Min, bool)
        Duplicate_ObjectY(context, amount, spacing, Min, bool)
        
        context.view_layer.objects.active = new_obj
    bpy.data.objects.remove(new_obj, do_unlink=True)


    
    

def StairGen(context, spacing, amount, direction):
    C = bpy.context
    
    for i in range(amount):
        if direction == "OP1":
            new = bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(spacing, spacing, spacing)})
            #bpy.ops.transform.rotate(value=-1.28491, orient_axis='Z', orient_type='VIEW', orient_matrix=((0.704497, 0.70958, -0.0134105), (-0.259485, 0.275122, 0.92573), (0.660569, -0.648694, 0.377948)), orient_matrix_type='VIEW', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
        elif direction == "OP2":
            new = bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(spacing, 0, spacing)})
        elif direction == "OP3":
            new = bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(-spacing, 0, spacing)})
        elif direction == "OP4":
            new = bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0, spacing, spacing)})
        elif direction == "OP5":
            new = bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0, -spacing, spacing)})
    
    


def DiamondGen(context, radius, amount):
    ob = context.object
    print("Before: ", ob)
    
    collection = bpy.data.collections.new("Diamond Gen")
    bpy.context.scene.collection.children.link(collection)
    

    Right = bpy.data.objects.new('Cube', ob.data)
    Right.location = ob.location
    Right.location.y += radius
    bpy.data.collections["Diamond Gen"].objects.link(Right)
    
    Left = bpy.data.objects.new('Cube', ob.data)
    Left.location = ob.location
    Left.location.x -= radius
    bpy.data.collections["Diamond Gen"].objects.link(Left)
    
    Top = bpy.data.objects.new('Cube', ob.data)
    Top.location = ob.location
    Top.location.x += radius
    bpy.data.collections["Diamond Gen"].objects.link(Top)
    
    Bottom = bpy.data.objects.new('Cube', ob.data)
    Bottom.location = ob.location
    Bottom.location.y -= radius
    bpy.data.collections["Diamond Gen"].objects.link(Bottom)

    
    for i in range(1, amount):
        step = radius/amount
        
        Right_Top = bpy.data.objects.new('Cube', ob.data)
        Right_Top.location = ob.location
        Right_Top.location.y += radius - step*i
        Right_Top.location.x += step*i
        bpy.data.collections["Diamond Gen"].objects.link(Right_Top)
        
        Right_Bottom = bpy.data.objects.new('Cube', ob.data)
        Right_Bottom.location = ob.location
        Right_Bottom.location.y += -(radius - step*i)
        Right_Bottom.location.x += step*i
        bpy.data.collections["Diamond Gen"].objects.link(Right_Bottom)
        
        Left_Top = bpy.data.objects.new('Cube', ob.data)
        Left_Top.location = ob.location
        Left_Top.location.y += -(radius - step*i)
        Left_Top.location.x -= step*i
        bpy.data.collections["Diamond Gen"].objects.link(Left_Top)
        
        Left_Bottom = bpy.data.objects.new('Cube', ob.data)
        Left_Bottom.location = ob.location
        Left_Bottom.location.y -= -(radius - step*i)
        Left_Bottom.location.x -= step*i
        bpy.data.collections["Diamond Gen"].objects.link(Left_Bottom)
        

    print("After: ", ob)



def SquareFrameY(context, amount):
    C = bpy.context
    save = bpy.context.active_object
    
    
    count = 1
    for i in range (0, amount-1):
        new_obj = bpy.context.active_object.copy()
        new_obj.animation_data_clear()
        print("New: ", new_obj.name)
        

        new_obj.location.y += 5
        C.collection.objects.link(new_obj)
        
    
        if count == amount-1:
            SquareFrameNegX(context, amount)
        count += 1
        
        
        context.view_layer.objects.active = new_obj
        
        
        
    context.view_layer.objects.active = save




def Tri_gen(context, spacing, amount, isEqual):
    C = bpy.context
    

    
    if isEqual:
        #For objects on Y axis
        for i in range(0, amount):
            new = bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0, spacing, 0)})
        #For objetcs on Left-Side edge
        for j in range(0, amount):
            next = bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(spacing/2, -spacing/2, 0)})
        #For objects on Right-Side edge
        for k in range(0, amount-1):
            new_next = bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(-spacing/2, -spacing/2, 0)})
    else:
        for i in range(0, amount):
            new = bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0, spacing, 0)})
        for j in range(0, amount):
            next = bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(spacing/amount, -spacing/2, 0)})
        for k in range(0, amount-1):
            new_next = bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(-spacing/amount, -spacing/2, 0)})






class SimpleOperator(bpy.types.Operator):
    bl_idname = "object.add_cube"
    bl_label = "Add A Cube"
    
    def execute(self, context):
        add_shapes(context)
        return { 'FINISHED' }



class addSphere(bpy.types.Operator):
    bl_idname = "object.add_sphere"
    bl_label = "Add A Sphere"
    
    def execute(self, context):
        add_sphere(context)
        return { 'FINISHED' }


class delObject(bpy.types.Operator):
    bl_idname = "object.delete"
    bl_label = "Delete"
    
    def execute(self, context):
        deleteObj(context)
        return { 'FINISHED' }




class copyObject(bpy.types.Operator):
    bl_idname = "object.grid"
    bl_label = "Generate 3D Grid"
    bl_options = { 'REGISTER', 'UNDO' }
    
    amount : bpy.props.IntProperty(default=1, min=1)
    spacing : bpy.props.FloatProperty(default=1, min=1)
    Minium : bpy.props.FloatProperty(default=1, min=1)
    
    def execute(self, context):
        scene = context.scene
        my_tool = scene.my_tool
        Duplicate_Object(context, self.amount, self.spacing, self.Minium, my_tool.my_bool)
        return { 'FINISHED' }



class Stair(bpy.types.Operator):
    bl_idname = "object.stair"
    bl_label = "Generate Stair"
    bl_options = { 'REGISTER', 'UNDO' }
    
    spacing : bpy.props.FloatProperty(default=1, min=1)
    amount : bpy.props.IntProperty(default=1, min=1)
    dir : bpy.props.EnumProperty(items=[("OP1", "Side Way", ""), ("OP2", "+x", ""), ('OP3', "-x", ""), ('OP4', "+y", ""), ('OP5', "-y", "")], name='Directions', default = None)
    

    def execute(self, context):
        StairGen(context, self.spacing, self.amount, self.dir)
        print(self.dir)
        return { 'FINISHED' }
        
        


class Diamond(bpy.types.Operator):
    bl_idname = "object.diamond"
    bl_label = "Generate Diamond"
    bl_options = { 'REGISTER', 'UNDO' }
    
    radius : bpy.props.FloatProperty(default=1, min=1)
    amount : bpy.props.IntProperty(default=1, min=1)
    

    def execute(self, context):
        DiamondGen(context, self.radius, self.amount)
        return { 'FINISHED' }



class Triangle(bpy.types.Operator):
    bl_idname = "object.triangle"
    bl_label = "Generate Triangle"
    bl_options = { 'REGISTER', 'UNDO' }
    
    spacing : bpy.props.FloatProperty(default=1, min=1)
    amount : bpy.props.IntProperty(default=1, min=1)

    def execute(self, context):
        scene = context.scene
        my_tool = scene.my_tool
        Tri_gen(context, self.spacing, self.amount, my_tool.Tri_equl)
        return { 'FINISHED' }

        



class LayoutDemoPanel(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_label = "Pattern Generator"
    bl_idname = "SCENE_PT_layout"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    #bl_context = "scene"
    bl_category = 'QOA'




    def draw(self, context):
        layout = self.layout
        scene = context.scene
        my_tool = scene.my_tool
        


        layout.label(text="Shape Adder")
        row = layout.row()
        row.scale_y = 2.0
        row.operator("object.add_cube")
        row = layout.row()
        row.scale_y = 2.0
        row.operator("object.add_sphere")
        row = layout.row()
        row.scale_y = 2.0
        row.operator("object.delete")
        row = layout.row()
        row.scale_y = 2.0
        row.operator("object.grid")
        
        layout.prop(my_tool, "my_bool", text="Randomize")
        
        row = layout.row()
        row.scale_y = 2.0
        row.operator("object.stair")
        
        row = layout.row()
        row.scale_y = 2.0
        row.operator("object.diamond")
        
        row = layout.row()
        row.scale_y = 2.0
        row.operator("object.triangle")
        
        layout.prop(my_tool, "Tri_equl", text="Equal")
        
        



def register():
    bpy.utils.register_class(myProperties)
    
    bpy.utils.register_class(Stair)
    bpy.utils.register_class(Diamond)
    bpy.utils.register_class(SimpleOperator)
    bpy.utils.register_class(addSphere)
    bpy.utils.register_class(delObject)
    bpy.utils.register_class(copyObject)
    bpy.utils.register_class(Triangle)
    bpy.utils.register_class(LayoutDemoPanel)
    
    bpy.types.Scene.my_tool = bpy.props.PointerProperty(type = myProperties)

def unregister():
    bpy.utils.unregister_class(SimpleOperator)
    bpy.utils.unregister_class(addSphere)
    bpy.utils.unregister_class(delObject)
    bpy.utils.unregister_class(copyObject)
    bpy.utils.unregister_class(Stair)
    bpy.utils.unregister_class(Diamond)
    bpy.utils.unregister_class(Triangle)
    bpy.utils.unregister_class(LayoutDemoPanel)
    
    del bpy.types.Scene.my_tool


if __name__ == "__main__":
    register()
