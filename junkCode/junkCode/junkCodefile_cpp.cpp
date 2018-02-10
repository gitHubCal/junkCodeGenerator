#include<iostream>
#include<string>
#include "outputFile.h"

namespace junkNamespace_7792 {
	junkClass_IrWjQ42::junkClass_IrWjQ42(int fUlLx5443) : junkCharArr_IrWjQ42(new char[1024]), junkInt_IrWjQ42(nullptr) { }
	junkClass_IrWjQ42::junkClass_IrWjQ42(float ccdpN527) : junkCharArr_IrWjQ42(new char[1024]), junkInt_IrWjQ42(nullptr) { };
	junkClass_IrWjQ42::junkClass_IrWjQ42(std::string bQmCr55, float OWVcl162, int NLGId44) : junkCharArr_IrWjQ42(new char[1024]), junkInt_IrWjQ42(new int(5)), bQmCr55(bQmCr55), OWVcl162(OWVcl162), NLGId44(NLGId44) { }
	junkClass_IrWjQ42::~junkClass_IrWjQ42() {
		delete[] junkCharArr_IrWjQ42; junkCharArr_IrWjQ42 = nullptr;
		delete junkInt_IrWjQ42; junkInt_IrWjQ42 = nullptr;
	}
	junkClass_IrWjQ42::junkClass_IrWjQ42(const junkClass_IrWjQ42& oldJunkObj) : junkCharArr_IrWjQ42(new char[1024]), junkInt_IrWjQ42(new int(*oldJunkObj.junkInt_IrWjQ42)), bQmCr55(oldJunkObj.bQmCr55), OWVcl162(oldJunkObj.OWVcl162), NLGId44(oldJunkObj.NLGId44) {
		*junkInt_IrWjQ42 = *oldJunkObj.junkInt_IrWjQ42;
		strcpy(junkCharArr_IrWjQ42, oldJunkObj.junkCharArr_IrWjQ42);
	}
	junkClass_IrWjQ42::junkClass_IrWjQ42(junkClass_IrWjQ42&& rValue) : junkCharArr_IrWjQ42(rValue.junkCharArr_IrWjQ42), junkInt_IrWjQ42(rValue.junkInt_IrWjQ42), bQmCr55(rValue.bQmCr55), OWVcl162(rValue.OWVcl162), NLGId44(rValue.NLGId44) {
		rValue.junkCharArr_IrWjQ42 = nullptr;
		rValue.junkInt_IrWjQ42 = nullptr;
		rValue.bQmCr55 = "";
	}
	junkClass_IrWjQ42& junkClass_IrWjQ42::operator=(const junkClass_IrWjQ42& toCopyAssign) {
		if(this != &toCopyAssign) {
			std::swap(*junkCharArr_IrWjQ42, *toCopyAssign.junkCharArr_IrWjQ42);
			std::swap(*junkInt_IrWjQ42, *toCopyAssign.junkInt_IrWjQ42);
			bQmCr55 = toCopyAssign.bQmCr55;
			OWVcl162 = toCopyAssign.OWVcl162;
			NLGId44 = toCopyAssign.NLGId44;
		}
		return *this;
	}
	junkClass_IrWjQ42& junkClass_IrWjQ42::operator=(junkClass_IrWjQ42&& toMove) {
		if(this != &toMove) {
			delete[] junkCharArr_IrWjQ42;
			delete junkInt_IrWjQ42;
			junkCharArr_IrWjQ42 = toMove.junkCharArr_IrWjQ42;
			junkInt_IrWjQ42 = toMove.junkInt_IrWjQ42;
		toMove.junkCharArr_IrWjQ42 = nullptr;
		toMove.junkInt_IrWjQ42 = nullptr;
			bQmCr55 = toMove.bQmCr55;
			OWVcl162 = toMove.OWVcl162;
			NLGId44 = toMove.NLGId44;
		}
		return *this;
	}
	int operator+(const junkClass_IrWjQ42& term_1, const junkClass_IrWjQ42& term_2) {
		return *term_1.junkInt_IrWjQ42 + *term_2.junkInt_IrWjQ42;
	}
	std::string junkClass_IrWjQ42::getString_bQmCr55() {
		return bQmCr55;
	}
	void junkClass_IrWjQ42::setString_bQmCr55(const std::string& newStr) {
		bQmCr55 = newStr;
	}
	float junkClass_IrWjQ42::getFloat_OWVcl162() {
		return OWVcl162;
	}
	void junkClass_IrWjQ42::setFloat_OWVcl162(float newFloat) {
		OWVcl162 = newFloat;
	}
	int junkClass_IrWjQ42::getInt_NLGId44() {
		return NLGId44;
	}
	void junkClass_IrWjQ42::setInt_NLGId44(int newInt) {
		NLGId44 = newInt;
	}
	float junkClass_IrWjQ42::generateRandFloat_Sxees45_2() {
		for(int i = 0; i < 66; i++) {
			continue;
		}
		float junkFloat_Sxees45 = 66.167;
		return junkFloat_Sxees45;
	}
	int junkClass_IrWjQ42::generateRandInt_lLugd76_1() {
		for(int i = 0; i < 17; i++) {
			continue;
		}
		int junkInt_lLugd76 = 17;
		return junkInt_lLugd76;
	}
	int junkClass_IrWjQ42::getJunkInt() {
		return *junkInt_IrWjQ42;
	}
};
namespace junkNamespace_9269 {
	junkClass_URKsg81::junkClass_URKsg81(int aYCxl5479) : junkCharArr_URKsg81(new char[1024]), junkInt_URKsg81(nullptr) { }
	junkClass_URKsg81::junkClass_URKsg81(float yGDDI1472) : junkCharArr_URKsg81(new char[1024]), junkInt_URKsg81(nullptr) { };
	junkClass_URKsg81::junkClass_URKsg81(std::string LaHYq147, float euJKr70, int FwJLN90) : junkCharArr_URKsg81(new char[1024]), junkInt_URKsg81(new int(1)), LaHYq147(LaHYq147), euJKr70(euJKr70), FwJLN90(FwJLN90) { }
	junkClass_URKsg81::~junkClass_URKsg81() {
		delete[] junkCharArr_URKsg81; junkCharArr_URKsg81 = nullptr;
		delete junkInt_URKsg81; junkInt_URKsg81 = nullptr;
	}
	junkClass_URKsg81::junkClass_URKsg81(const junkClass_URKsg81& oldJunkObj) : junkInt_URKsg81(new int(*oldJunkObj.junkInt_URKsg81)), LaHYq147(oldJunkObj.LaHYq147), euJKr70(oldJunkObj.euJKr70), FwJLN90(oldJunkObj.FwJLN90) {
		*junkInt_URKsg81 = *oldJunkObj.junkInt_URKsg81;
		junkCharArr_URKsg81 = new char[1024];
		strcpy(junkCharArr_URKsg81, oldJunkObj.junkCharArr_URKsg81);
	}
	junkClass_URKsg81::junkClass_URKsg81(junkClass_URKsg81&& rValue) : junkCharArr_URKsg81(rValue.junkCharArr_URKsg81), junkInt_URKsg81(rValue.junkInt_URKsg81), LaHYq147(rValue.LaHYq147), euJKr70(rValue.euJKr70), FwJLN90(rValue.FwJLN90) {
		rValue.junkCharArr_URKsg81 = nullptr;
		rValue.junkInt_URKsg81 = nullptr;
		rValue.LaHYq147 = "";
	}
	junkClass_URKsg81& junkClass_URKsg81::operator=(const junkClass_URKsg81& toCopyAssign) {
		if(this != &toCopyAssign) {
			std::swap(*junkCharArr_URKsg81, *toCopyAssign.junkCharArr_URKsg81);
			std::swap(*junkInt_URKsg81, *toCopyAssign.junkInt_URKsg81);
			LaHYq147 = toCopyAssign.LaHYq147;
			euJKr70 = toCopyAssign.euJKr70;
			FwJLN90 = toCopyAssign.FwJLN90;
		}
		return *this;
	}
	junkClass_URKsg81& junkClass_URKsg81::operator=(junkClass_URKsg81&& toMove) {
		if(this != &toMove) {
			delete[] junkCharArr_URKsg81;
			delete junkInt_URKsg81;
			junkCharArr_URKsg81 = toMove.junkCharArr_URKsg81;
			junkInt_URKsg81 = toMove.junkInt_URKsg81;
		toMove.junkCharArr_URKsg81 = nullptr;
		toMove.junkInt_URKsg81 = nullptr;
			LaHYq147 = toMove.LaHYq147;
			euJKr70 = toMove.euJKr70;
			FwJLN90 = toMove.FwJLN90;
		}
		return *this;
	}
	int operator+(const junkClass_URKsg81& term_1, const junkClass_URKsg81& term_2) {
		return *term_1.junkInt_URKsg81 + *term_2.junkInt_URKsg81;
	}
	std::string junkClass_URKsg81::getString_LaHYq147() {
		return LaHYq147;
	}
	void junkClass_URKsg81::setString_LaHYq147(const std::string& newStr) {
		LaHYq147 = newStr;
	}
	float junkClass_URKsg81::getFloat_euJKr70() {
		return euJKr70;
	}
	void junkClass_URKsg81::setFloat_euJKr70(float newFloat) {
		euJKr70 = newFloat;
	}
	int junkClass_URKsg81::getInt_FwJLN90() {
		return FwJLN90;
	}
	void junkClass_URKsg81::setInt_FwJLN90(int newInt) {
		FwJLN90 = newInt;
	}
	float junkClass_URKsg81::generateRandFloat_GkHZd51_2() {
		for(int i = 0; i < 43; i++) {
			continue;
		}
		float junkFloat_GkHZd51 = 43.146;
		return junkFloat_GkHZd51;
	}
	int junkClass_URKsg81::generateRandInt_GvBQM17_1() {
		for(int i = 0; i < 77; i++) {
			continue;
		}
		int junkInt_GvBQM17 = 77;
		return junkInt_GvBQM17;
	}
	int junkClass_URKsg81::getJunkInt() {
		return *junkInt_URKsg81;
	}
};
namespace junkNamespace_5937 {
	junkClass_uIDxr94::junkClass_uIDxr94(int otNWt4829) : junkCharArr_uIDxr94(new char[1024]), junkInt_uIDxr94(nullptr) { }
	junkClass_uIDxr94::junkClass_uIDxr94(float dIxIP827) : junkCharArr_uIDxr94(new char[1024]), junkInt_uIDxr94(nullptr) { };
	junkClass_uIDxr94::junkClass_uIDxr94(std::string ASWJm82, float vXPBR51, int DLfla48) : junkCharArr_uIDxr94(new char[1024]), junkInt_uIDxr94(new int(3)), ASWJm82(ASWJm82), vXPBR51(vXPBR51), DLfla48(DLfla48) { }
	junkClass_uIDxr94::~junkClass_uIDxr94() {
		delete[] junkCharArr_uIDxr94; junkCharArr_uIDxr94 = nullptr;
		delete junkInt_uIDxr94; junkInt_uIDxr94 = nullptr;
	}
	junkClass_uIDxr94::junkClass_uIDxr94(const junkClass_uIDxr94& oldJunkObj) : junkInt_uIDxr94(new int(*oldJunkObj.junkInt_uIDxr94)), ASWJm82(oldJunkObj.ASWJm82), vXPBR51(oldJunkObj.vXPBR51), DLfla48(oldJunkObj.DLfla48) {
		*junkInt_uIDxr94 = *oldJunkObj.junkInt_uIDxr94;
		junkCharArr_uIDxr94 = new char[1024];
		strcpy(junkCharArr_uIDxr94, oldJunkObj.junkCharArr_uIDxr94);
	}
	junkClass_uIDxr94::junkClass_uIDxr94(junkClass_uIDxr94&& rValue) : junkCharArr_uIDxr94(rValue.junkCharArr_uIDxr94), junkInt_uIDxr94(rValue.junkInt_uIDxr94), ASWJm82(rValue.ASWJm82), vXPBR51(rValue.vXPBR51), DLfla48(rValue.DLfla48) {
		rValue.junkCharArr_uIDxr94 = nullptr;
		rValue.junkInt_uIDxr94 = nullptr;
		rValue.ASWJm82 = "";
	}
	junkClass_uIDxr94& junkClass_uIDxr94::operator=(const junkClass_uIDxr94& toCopyAssign) {
		if(this != &toCopyAssign) {
			std::swap(*junkCharArr_uIDxr94, *toCopyAssign.junkCharArr_uIDxr94);
			std::swap(*junkInt_uIDxr94, *toCopyAssign.junkInt_uIDxr94);
			ASWJm82 = toCopyAssign.ASWJm82;
			vXPBR51 = toCopyAssign.vXPBR51;
			DLfla48 = toCopyAssign.DLfla48;
		}
		return *this;
	}
	junkClass_uIDxr94& junkClass_uIDxr94::operator=(junkClass_uIDxr94&& toMove) {
		if(this != &toMove) {
			delete[] junkCharArr_uIDxr94;
			delete junkInt_uIDxr94;
			junkCharArr_uIDxr94 = toMove.junkCharArr_uIDxr94;
			junkInt_uIDxr94 = toMove.junkInt_uIDxr94;
		toMove.junkCharArr_uIDxr94 = nullptr;
		toMove.junkInt_uIDxr94 = nullptr;
			ASWJm82 = toMove.ASWJm82;
			vXPBR51 = toMove.vXPBR51;
			DLfla48 = toMove.DLfla48;
		}
		return *this;
	}
	int operator+(const junkClass_uIDxr94& term_1, const junkClass_uIDxr94& term_2) {
		return *term_1.junkInt_uIDxr94 + *term_2.junkInt_uIDxr94;
	}
	std::string junkClass_uIDxr94::getString_ASWJm82() {
		return ASWJm82;
	}
	void junkClass_uIDxr94::setString_ASWJm82(const std::string& newStr) {
		ASWJm82 = newStr;
	}
	float junkClass_uIDxr94::getFloat_vXPBR51() {
		return vXPBR51;
	}
	void junkClass_uIDxr94::setFloat_vXPBR51(float newFloat) {
		vXPBR51 = newFloat;
	}
	int junkClass_uIDxr94::getInt_DLfla48() {
		return DLfla48;
	}
	void junkClass_uIDxr94::setInt_DLfla48(int newInt) {
		DLfla48 = newInt;
	}
	float junkClass_uIDxr94::generateRandFloat_drUFJ121_2() {
		for(int i = 0; i < 82; i++) {
			continue;
		}
		float junkFloat_drUFJ121 = 82.122;
		return junkFloat_drUFJ121;
	}
	int junkClass_uIDxr94::generateRandInt_ovolM40_1() {
		for(int i = 0; i < 52; i++) {
			continue;
		}
		int junkInt_ovolM40 = 52;
		return junkInt_ovolM40;
	}
	int junkClass_uIDxr94::getJunkInt() {
		return *junkInt_uIDxr94;
	}
};
namespace junkNamespace_1218 {
	int UZRRb358(int& MJELe225, int& zCKPb53) {
		for(int i = 23; i<100; i++) {
			continue;
		}
		for(int i = 2; i<100; i++) {
			continue;
		}
		for(int i = 96; i<100; i++) {
			continue;
		}
		int count_vsSOo50 = 10;
		while(count_vsSOo50>0) {
			count_vsSOo50--;
			continue;
		}
		for(int i = 4; i<100; i++) {
			continue;
		}
		for(int i = 26; i<100; i++) {
			continue;
		}
		int KmRYD161;
		char WhBuh187;
		float uGwZA24;
		int JjJJO21667;
		return JjJJO21667;

	}
	std::string dbJVc301(int& RcqPX43) {
		for(int i = 88; i<100; i++) {
			continue;
		}
		for(int i = 19; i<100; i++) {
			continue;
		}
		for(int i = 74; i<100; i++) {
			continue;
		}
		int count_OWEyK67 = 19;
		while(count_OWEyK67>0) {
			count_OWEyK67--;
			continue;
		}
		for(int i = 45; i<100; i++) {
			continue;
		}
		for(int i = 21; i<100; i++) {
			continue;
		}
		double KnBMg114;
		int KAFmD172;
		double vLIvk66;
		std::string PyyTK20670;
		return PyyTK20670;

	}
	float MvWpA108() {
		for(int i = 73; i<100; i++) {
			continue;
		}
		for(int i = 52; i<100; i++) {
			continue;
		}
		for(int i = 46; i<100; i++) {
			continue;
		}
		int count_oXLFx139 = 1;
		while(count_oXLFx139>0) {
			count_oXLFx139--;
			continue;
		}
		for(int i = 55; i<100; i++) {
			continue;
		}
		for(int i = 13; i<100; i++) {
			continue;
		}
		int Wwsnt47;
		float gGKNo8;
		std::string VrzlW65;
		float OnQEN36676;
		return OnQEN36676;

	}
};

int main() {
	std::string randStr = "Hello";
	std::string randStr2 = "cal";
	junkNamespace_7792::junkClass_IrWjQ42 A(randStr, 1.0f, 2);
	junkNamespace_7792::junkClass_IrWjQ42 B(randStr2, 2.9f, 3);
	int result2 = A + B;
	std::cout << result2 << std::endl;
	/*A = B;*/
	A = std::move(B);
	std::cout << A.getJunkInt() << std::endl;
	junkNamespace_7792::junkClass_IrWjQ42 C = A;
	junkNamespace_7792::junkClass_IrWjQ42 D = std::move(A);
	std::cout << D.getJunkInt() << std::endl;
	junkNamespace_7792::junkClass_IrWjQ42 E(1.23f);
	junkNamespace_5937::junkClass_uIDxr94 A1(randStr, 2.0f, 3);
	junkNamespace_5937::junkClass_uIDxr94 A2(randStr2, 3.0f, 1);
	int result = A1 + A2;
	std::cout << result << std::endl;
	return 0;
}