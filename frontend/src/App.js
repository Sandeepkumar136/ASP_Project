import React, { useState } from "react";
import axios from "axios";

function App() {
    const [message, setMessage] = useState("");

    const handlePost = async () => {
        try {
            if (!message.trim()) {
                alert("Message cannot be empty!");
                return;
            }

            const response = await axios.post("http://127.0.0.1:5000/post", { message });
            alert(response.data.message);
            setMessage(""); // Clear input after successful post
        } catch (error) {
            console.error("Error posting message:", error);
            alert("Failed to post. Check console for details.");
        }
    };

    return (
        <div>
            <h1>Social Media Poster</h1>
            <textarea 
                value={message} 
                onChange={(e) => setMessage(e.target.value)} 
                placeholder="Type your message here..."
            />
            <button onClick={handlePost}>Post</button>
        </div>
    );
}

export default App;
