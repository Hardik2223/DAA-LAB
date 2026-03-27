try:
    import tensorflow as tf
    from tensorflow import keras
except ImportError:
    tf = None

if __name__ == "__main__":
    if tf is None:
        print("TensorFlow is not installed")
    else:
        model = keras.Sequential([
            keras.layers.Dense(16, activation='relu', input_shape=(4,)),
            keras.layers.Dense(3, activation='softmax')
        ])
        model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
        import numpy as np
        x = np.random.randn(10, 4)
        y = np.random.randint(0, 3, 10)
        model.fit(x, y, epochs=2, verbose=0)
        print("Model built and briefly trained")
