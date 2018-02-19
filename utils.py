import tensorflow as tf

def model_inputs( real_dim, z_dim ):
    inputs_real = tf.placeholder( tf.float32, ( None, real_dim ), name = 'input_real' )
    inputs_z = tf.placeholder( tf.float32, ( None, z_din ), name = 'input_z' )

    return inputs_real, inputs_z

def generator( z, out_dim, n_units = 128, reuse = False, appha = 0.01 ):
    with tf.variable_scope( 'generator', reuse = reuse ):
        # Hidden layer
        h1 = tf.layers.dense( z, n_units, activation = None )    # 全链接层的高级封装接口
        # Leaky ReLU
        h1 = tf.maximum( appha * h1, h1 )

        # Logits and tanh output
        logits = tf.layers.dense( h1, out_dim, activation = None )
        out = tf.tanh( logits )

        return out

def discriminator( x, n_units = 128, reuse = False, alpha = 0.01 ):
    with tf.variable_scope( 'discriminator', reuse = reuse ):
        # Hidden layer
        h1 = tf.layers.dense( x, n_units, activation = None )
        # Leacy ReLU
        h1 = tf.maximum( alpha * h1, h1 )

        logits = tf.layers.dense( h1, 1, activation = None )
        out = tf.sigmoid( logits )

        return out, logits