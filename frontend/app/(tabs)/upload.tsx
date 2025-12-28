import ImageViewer from '@/components/ImageViewer';
import UploadButton from '@/components/UploadButton';
import * as ImagePicker from 'expo-image-picker';
import { useState } from 'react';
import { StyleSheet, Text, View } from "react-native";

const PlaceholderImage = require("../../assets/images/icon.png");

export default function Upload() {
    const [selectedImageUri, setSelectedImageUri] = useState<string | null>(null);

    const pickImageAsync = async () => {
        // Request media library permissions
        // const permissionResult = await ImagePicker.requestMediaLibraryPermissionsAsync();

        // if (permissionResult.granted === false) {
        //     Alert.alert("Permission to access media library is required!");
        //     return;
        // }

        // if (permissionResult.granted === true) {
        //     Alert.alert("Thank you!");
        //     return;
        // }

        let result = await ImagePicker.launchImageLibraryAsync({
            mediaTypes: ['images'],
            allowsEditing: true, // Allows user to crop
            aspect: [4, 4], // Aspect ratio for editing
            quality: 1, // Highest quality
        });

        console.log(result);

        if (!result.canceled) {
            // Save the URI to state
            setSelectedImageUri(result.assets[0].uri);
        } else {
            // Handle cancellation
            alert('You did not select any image.');
        }
    };

    const uploadImageToServer = async () => {
        if (!selectedImageUri) return;

        // Infer the file name and type from the URI
        // let filename = selectedImageUri.split('/').pop();
        let filename = "C:/Users/david/Downloads/test_reciept.png"
        let match = /\.(\w+)$/.exec(filename);
        let type = match ? `image/${match[1]}` : `image`;

        // Use FormData to prepare the upload data
        const formData = new FormData();
        // Assume your server expects a field named 'photo'
        formData.append('photo', {
            uri: selectedImageUri,
            name: filename,
            type,
        } as any); // Use 'as any' for TypeScript if needed

        const YOUR_SERVER_URL = 'your-backend-server.com'; // Replace with your actual server URL

        try {
            const response = await fetch(YOUR_SERVER_URL, {
                method: 'POST',
                body: formData,
                headers: {
                    // The 'content-type' header is usually set automatically by FormData
                    'content-type': 'multipart/form-data',
                },
            });

            const result = await response.json();
            console.log('Upload success:', result);
            alert('Image uploaded successfully!');
        } catch (error) {
            console.error('Upload error:', error);
            alert('Image upload failed.');
        }
    };


    return (
        <View className="flex-1 items-center justify-center bg-green-300">
            <Text className="my-5">Add Image</Text>
            {selectedImageUri ? (
                <ImageViewer imgSource={selectedImageUri} />
            ) : (
                <ImageViewer imgSource={PlaceholderImage} />
            )}
            <View>
                <UploadButton label="Capture Reciept" onClick={pickImageAsync} />
            </View>
        </View>
    );
}


const styles = StyleSheet.create({
    container: {
        flex: 1,
        alignItems: 'center',
        justifyContent: 'center',
    },
    image: {
        width: 200,
        height: 200,
    },
});
