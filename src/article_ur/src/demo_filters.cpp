// #include "ii"

// // init filter
// Iir::Butterworth::LowPass<order> f;  // NOTE： here order should replaced by a int number!
// const float samplingrate = 1000; // Hz
// const float cutoff_frequency = 5; // Hz
// f.setup (order, samplingrate, cutoff_frequency); // NOTE： here order should replaced by a int number!

// // Realtime filtering sample by sample
// float y = f.filter(x); // here x is a float, and one dimension
#include <ur_rtde/rtde_control_interface.h>
#include <ur_rtde/rtde_io_interface.h>
#include <ur_rtde/rtde_receive_interface.h>
#include <thread>
#include <chrono>

using namespace ur_rtde;
int main(int argc, char* argv[])
{
RTDEReceiveInterface rtde_receive("192.168.3.101");
std::vector<double> joint_positions = rtde_receive.getActualQ();
for(int i=0;i<6;i++)
{
    std::cout<<joint_positions[i]<<" ";
}
std::cout<<std::endl;


}

