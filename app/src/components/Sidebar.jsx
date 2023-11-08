import React from "react";

const Sidebar = ({ scene, setScene, mode, setMode }) => {
  return (
    <aside className="duration-500 ease-in-out z-50 hover:w-3/6 w-[13.66%] h-full fixed bg-red-800 text-white shadow-xl flex flex-col text-lg font-medium justify-between pt-32 pb-10 sm:w-1/12 sm:hover:w-4/12 lg:w-[5%] lg:hover:w-2/12 group">
      <div className="w-full h-3/6 flex flex-col gap-1 items-center justify-center">
        <div
          className={`flex gap-3 w-3/4 px-4 py-3 items-center duration-500 ease-in-out rounded-lg hover:shadow-md cursor-pointer ${
            scene === 0 ? "bg-red-500" : "hover:bg-red-500"
          }`}
          onClick={() => {
            setScene(0);
          }}
        >
          <i className="fa-solid fa-gauge text-white"></i>
          <span className="group-hover:text-lg duration-500 ease-in-out text-[0px]">
            Dashboard
          </span>
        </div>
        <div
          className={`flex gap-3 w-3/4 px-4 py-3 items-center duration-500 ease-in-out rounded-lg hover:shadow-md cursor-pointer ${
            scene === 1 ? "bg-red-500" : "hover:bg-red-500"
          }`}
          onClick={() => {
            setScene(1);
          }}
        >
          <i className="fa-solid fa-user text-white"></i>
          <span className="group-hover:text-lg duration-500 ease-in-out text-[0px]">
            Insigths
          </span>
        </div>
        <div className="flex gap-3 w-3/4 px-2 py-3 items-center">
          <div className="flex justify-center items-center">
            <div
              className={mode ? "hidden" : ""}
              onClick={() => {
                localStorage.mode = !mode;
                setMode(!mode);
              }}
            >
              <i className="fa-solid fa-sun w-8 p-2 text-center rounded-full bg-white text-red-800 cursor-pointer hover:text-white hover:bg-red-700 duration-500 ease-in-out "></i>
            </div>
            <div
              className={mode ? "" : "hidden"}
              onClick={() => {
                localStorage.mode = !mode;
                setMode(!mode);
              }}
            >
              <i className="fa-solid fa-moon w-8 p-2 text-center rounded-full bg-red-800 text-white cursor-pointer hover:text-red-800 hover:bg-white duration-500 ease-in-out"></i>
            </div>
          </div>
        </div>
      </div>
    </aside>
  );
};

export default Sidebar;
