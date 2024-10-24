import React, { useState, useEffect } from 'react';
import './AdminPage.css';

const AdminPage = () => {
    const [users, setUsers] = useState([]);
    const [newUser, setNewUser] = useState({ username: '', email: '', password: '' });
    const [editUser, setEditUser] = useState(null);

    useEffect(() => {
        fetchUsers();
    }, []);

    const fetchUsers = async () => {
        // const response = await fetch('http://localhost:8000/users');
        // const data = await response.json();
        // setUsers(data);
    };

    const handleCreateUser = async (e) => {
        // e.preventDefault();
        // const response = await fetch('http://localhost:8000/users', {
        //     method: 'POST',
        //     headers: { 'Content-Type': 'application/json' },
        //     body: JSON.stringify(newUser),
        // });
        // if (response.ok) {
        //     fetchUsers();
        //     setNewUser({ username: '', email: '', password: '' });
        // }
    };

    const handleUpdateUser = async (e) => {
        e.preventDefault();
        // const response = await fetch(`http://localhost:8000/users/${editUser.id}`, {
        //     method: 'PUT',
        //     headers: { 'Content-Type': 'application/json' },
        //     body: JSON.stringify(editUser),
        // });
        // if (response.ok) {
        //     fetchUsers();
        //     setEditUser(null);
        // }
    };

    const handleDeleteUser = async (userId) => {
        // const response = await fetch(`http://localhost:8000/users/${userId}`, {
        //     method: 'DELETE',
        // });
        // if (response.ok) {
        //     fetchUsers();
        // }
    };

    return (
        <div className="admin-container">
            <h1>Admin Dashboard</h1>
            <h2>Manage Accounts</h2>

            <form onSubmit={handleCreateUser}>
                <h3>Create User</h3>
                <input
                    type="text"
                    placeholder="Username"
                    value={newUser.username}
                    onChange={(e) => setNewUser({ ...newUser, username: e.target.value })}
                    required
                />
                <input
                    type="email"
                    placeholder="Email"
                    value={newUser.email}
                    onChange={(e) => setNewUser({ ...newUser, email: e.target.value })}
                    required
                />
                <input
                    type="password"
                    placeholder="Password"
                    value={newUser.password}
                    onChange={(e) => setNewUser({ ...newUser, password: e.target.value })}
                    required
                />
                <button type="submit">Create</button>
            </form>

            {editUser && (
                <form onSubmit={handleUpdateUser}>
                    <h3>Edit User</h3>
                    <input
                        type="text"
                        placeholder="Username"
                        value={editUser.username}
                        onChange={(e) => setEditUser({ ...editUser, username: e.target.value })}
                    />
                    <input
                        type="email"
                        placeholder="Email"
                        value={editUser.email}
                        onChange={(e) => setEditUser({ ...editUser, email: e.target.value })}
                    />
                    <button type="submit">Update</button>
                    <button type="button" onClick={() => setEditUser(null)}>Cancel</button>
                </form>
            )}

            <h3>Current Users</h3>
            <ul>
                {users.map(user => (
                    <li key={user.id}>
                        {user.username} ({user.email})
                        <button onClick={() => setEditUser(user)}>Edit</button>
                        <button onClick={() => handleDeleteUser(user.id)}>Delete</button>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default AdminPage;