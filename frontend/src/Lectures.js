import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Lecture = () => {
    const [lecture, setLecture] = useState(null);

    useEffect(() => {
        // Replace with your Flask API URL and lecture ID
        const fetchData = async () => {
            const result = await axios.get('http://127.0.0.1:5000/lecture/1');
            setLecture(result.data);
        };

        fetchData();
    }, []);

    return (
        <div>
            {lecture ? (
                <>
                    <h1>{lecture.title}</h1>
                    <p>{lecture.description}</p>
                    <p>{lecture.upload_date}</p>
                    {/* Render other lecture details */}
                </>
            ) : (
                <p>Loading...</p>
            )}
        </div>
    );
};

export default Lecture;
